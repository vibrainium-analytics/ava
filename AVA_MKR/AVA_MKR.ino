/*
  Automotive Vibration Analyizer MKR1000 wireless data acquisition
  Written by Vibranium Analytics
  
  As part of a wireless battery powered sensor package this program will sample values from a 
  3- axis accelerometer at 500 samples per second (500Hz)for approximately 8 seconds at a time.
  The actual length of sampling is 4096 samples which equals 8.2 seconds.  The number 4096 was chosen 
  because it is a power of 2 and translates efficiently to a fast fourier transform for frequency 
  analysis.  Sampling for longer that 8 seconds is accomplished by using a loop in the parent program 
  allowing for a sample length of any multiple of 8.2 seconds. 
  
  The program can sample axes one at a time, or all three at once.  
  Additional features include:
    Accelerometer self test feature 
    Time-out reset if no requests are recieved for 2.5 minutes
    Ten second delay that when used with a loop in the data acquisition program can be extended to 
      any multiple of ten seconds to allow vehicle to reach a desired state prior to sampling of 
      vibration data.

  The sampled values are transmitted over a Wi-Fi connection to a local IP address 
  where the data can be viewed. For example:
    if the default IP address of your shield is http://192.168.1.1
    http://192.168.1.1    Would display the menu screen.
    http://192.168.1.1/A  Would send data from each of the 3 axes.
    http://192.168.1.1/X  Would send data from the X axis only.  etc...

*/

#include <SPI.h> 
#include <WiFi101.h>

int led =  LED_BUILTIN;             // used to turn LED on 
int count = 0;                      // inactivity counter
<<<<<<< HEAD
char ssid[] = "AVA-Sensor";         // wireless access point name
=======
char ssid[] = "wifi101-network";    // wireless access point name
>>>>>>> 70eb98ffa6e6d81118ded3bf2cc7e3403f7ac338
String currentLine;                 // stores incomming data
short cnt3 = 60;                    // number of times to run outer loop
short cnt2 = 20;                    // number of times to run middle loop
short cnt1 = 25;                    // number of times to run inner loop when sampling one axis
short cnta = 8;                     // number of times to run inner loop sampling all 3 axes                         
short datax[50];                    // holds x axis samples 
short datay[50];                    // holds y axis samples
short dataz[50];                    // holds z axis samples
short r = 1757;                     // sample delay for sampling 3 axes 
char nl = '\n';                     // new line character for formatting 
char sp = ' ';                      // space character for formatting   
int status = WL_IDLE_STATUS;
WiFiServer server(80);              // Server will be on port 80

void setup() {

  analogReadResolution(12);                         // Sets number of bits for resolution of ADC (max 12)
  ADC->CTRLB.reg = ADC_CTRLB_PRESCALER_DIV32;       // Sets ADC clock delay (lowest recommended is 16 microseconds)
  pinMode(led, OUTPUT);                             // set the LED pin mode
  pinMode(9, OUTPUT);                               // digital pin used for reset feature
  digitalWrite(9,1);                                // pin must be on unless a reset is requested
  pinMode(11, OUTPUT);                              // digital pin used for accelerometer self test
  status = WiFi.beginAP(ssid);                      // Create open network. (no password required)
  delay(10000);                                     // wait 10 seconds for connection:
  server.begin();                                   // start the web server
}

void loop() {
  
  digitalWrite(led, HIGH);                          // turns the LED on
  digitalWrite(9,HIGH);                             // pin must be high unless a reset is requested
  WiFiClient client = server.available();           // listen for incoming clients
  if (client) {                                     
    currentLine = "";                               // initialize incoming data string
    while (client.connected()) {                    // loop while the client is connected  
      if (client.available()) {                     // if there are bytes to read from the client,
        char in = client.read();                    // read a byte
        if (in == '\n') {                           // check if the byte is a newline character

          // if the current line length is zero the line is blank and you got two newline characters in a row.
          // that's the end of the client HTTP request, so send a response:
          
          if (currentLine.length() == 0) {
            
            // HTTP headers always start with a response code (e.g. HTTP/1.1 200 OK)
            // then a content-type so the client knows what's coming, followed by a blank line
            
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println();

            // the content of the HTTP response follows the header
            
            client.print("Click <a href=\"/A\">here</a> to request data from all three axes <br>");
            client.print("Click <a href=\"/D\">here</a> to delay (10 seconds) <br>");
            client.print("Click <a href=\"/S\">here</a> to run accelerometer self test<br>");
            client.print("Click <a href=\"/X\">here</a> to request x axis data<br>");
            client.print("Click <a href=\"/Y\">here</a> to request y axis data<br>");
            client.print("Click <a href=\"/Z\">here</a> to request z axis data<br>");
            
            client.println();                       // The HTTP response ends with a blank line:
            break;                                  // break out of the while loop
          }
          else {
            currentLine = "";                       // after recieving a newline, clear currentLine
          }
        }
        else if (in != '\r') {                      // if you got anything else but a carriage return
          currentLine += in;                        // add it to the end of the currentLine (this is input from the user)         
        }

        if (currentLine.endsWith("GET /A")) {
          
          // User requested data, Send header
          
          client.println("HTTP/1.1 200 OK");
          client.println("Content-type:text/html");
          client.println();
          
          // data acquisition        
          
          int c2 = 2*cnta;                          // calculate number of times to run middle loop (16)
          int c3 = 4*cnta;                          // calculate number of times to run outer loop (32)           
          int l = 0;                                // initialize outer loop counter
          while (l != c3){                    
            int k=0;                                // initialize mid loop counter
            while (k != c2){  
              String csv = "";                      // initialize to blank string
              // take first sample 
              datax[1] = analogRead(A0);
              datay[1] = analogRead(A1);
              dataz[1] = analogRead(A2); 
              int j = 1;                            // Initialize loop inner loop counter 
              int c1 = cnta;                        
              while (j != c1){
                j++;
                delayMicroseconds(r);               // Delay to ensure sample every .002 seconds (500Hz)
                datax[j] = analogRead(A0);
                datay[j] = analogRead(A1);
                dataz[j] = analogRead(A2);              
              }
              
              // place integer data into string. cnta is chosen so that the transfer will take r microseconds
              
              j = 1;                                
              while (j != cnta) {
                csv = csv + String(datax[j])+ sp + String(datay[j]) + sp + String(dataz[j]) + sp3 + nl;
                j ++;
              }
              //read one more sample
              datax[j] = analogRead(A0);
              datay[j] = analogRead(A1);
              dataz[j] = analogRead(A2);
              csv = csv + String(datax[j])+ sp + String(datay[j]) + sp + String(dataz[j]) + nl;
              client.print(csv);                    // print the data to the IP address (this should also take r microseconds)
              k++;                                  
            }
            l++;                                    
          }
          currentLine = "";                         // reset current line to prepare for next request
          client.println();                         // The HTTP response ends with a blank line:
          count = 0;                                // reset inactivity counter
          break;                                    // break out of the while loop
        }

        if (currentLine.endsWith("GET /D")) {
          
          //Header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-type:text/html");
          client.println();

          // one minute countdown
          client.print("10<br>");
          delay(10000);
          client.print("0<br>");
          currentLine = "";
          client.println();
          count = 0;                                // reset inactivity counter
          break;        
        }
          
         if (currentLine.endsWith("GET /S")){
          
          // User requested data, Send header 
          client.println("HTTP/1.1 200 OK");
          client.println("Content-type:text/html");
          client.println();
          
          String message = Self_test();             // Get results from Self_test function
          client.print(message);
          currentLine = "";                         // reset current line to prepare for next request
          client.println();                         
          count = 0;                                // reset inactivity counter
          break;                                    
         }
        
        if (currentLine.endsWith("GET /X")) {
          
          // User requested data, Send header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-type:text/html");
          client.println();
          
          short l = 0;                              // initialize outer loop counter
          while (l != cnt3){                    
            short k=0;                              // initialize mid loop counter
            while (k != cnt2){  
              String csv = "";                      // initialize to blank string
              csv = data_read('X');                 // get results from data_read function
              client.print(csv);                    // print the data to the IP address (this should also take q microseconds)
              k++;                                  // increment the middle loop
            }
            l++;                                    // increment the outer loop
          }
          currentLine = "";                         // reset current line to prepare for next request
          client.println();                         // The HTTP response ends with a blank line:
          count = 0;                                // reset inactivity counter
          break;                                    // break out of the while loop
        }        

        if (currentLine.endsWith("GET /Y")) {
          // User requested data, Send header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-type:text/html");
          client.println();
          short l = 0;                              // initialize outer loop counter
          while (l != cnt3){                    
            short k=0;                              // initialize mid loop counter
            while (k != cnt2){  
              String csv = "";                      // initialize to blank string
              csv = data_read('Y');                 // get results from data_read function
              client.print(csv);                    // print the data to the IP address (this should also take q microseconds)
              k++;                                  // increment the middle loop
            }
            l++;                                    // increment the outer loop
          }
          currentLine = "";                         // reset current line to prepare for next request
          client.println();                         // The HTTP response ends with a blank line:
          count = 0;                                // reset inactivity counter
          break;                                    // break out of the while loop
        }

        if (currentLine.endsWith("GET /Z")) {
          // User requested data, Send header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-type:text/html");
          client.println();
          short l = 0;                              // initialize outer loop counter
          while (l != cnt3){                    
            short k=0;                              // initialize mid loop counter
            while (k != cnt2){  
              String csv = "";                      // initialize to blank string
              csv = data_read('Z');                 // get results from data_read function
              client.print(csv);                    // print the data to the IP address (this should also take q microseconds)
              k++;                                  // increment the middle loop
            }
            l++;                                    // increment the outer loop
          }
          currentLine = "";                         // reset current line to prepare for next request
          client.println();                         // The HTTP response ends with a blank line:
          count = 0;                                // reset inactivity counter
          break;                                    // break out of the while loop
        } 
      }
    }

    // close the connection:
    client.stop();  
  }
  if (count >= 15000000){                           // approximate number of loops in 2.5 minutes
    digitalWrite(9, LOW);                           // if there is no client request for 2.5 minutes the unit resets itself
  }
  count++;
}


/* data_read function.  
 * 
 * Recieves the value of the axis to read, logs 25 samples, writes them to a string separated by 
 * new line characters, and returns the string. New line characters are selected for data 
 * formatting into a text file.
 * 
 * The data read and string conversion are done separately because the string converstion takes 
 * longer each time it is concatonated.  
 * By logging the data first the delay between samples is constant.
 */
 
String data_read(char axis) {
  short pin;
  short d = 1962;                         // Delay setting for 500Hz sample rate
  String csv = "";
  short data[25];
  short j = 1;                            // Initialize loop inner loop counter (must be 1 to hold data in array position 1) 
  short c1 = 24;                          // loop will log 24 samples (1 to 25)
  // set pin to read
  if (axis == 'X'){
    pin = 0;                  
  }
  else if (axis == 'Y'){
    pin = 1;
  }
  else if (axis == 'Z'){
    pin = 2;
  }
  else {
    csv = "error no axis selected";
  }
    // read first sample 
  data[1] = analogRead(pin);  
  while (j != c1){
    j++;
    delayMicroseconds(d);                 // Delay to ensure sample every .002 seconds (500Hz)
    data[j] = analogRead(pin);            // Read data
  }
  j = 1;                                  // Use the same counter to transfer from array to string
  while (j != c1+1) {
    csv = csv + String(data[j])+ '\n';
    j ++;
  }
  //read 25th sample and write it to the string
  data[j] = analogRead(pin);
  csv = csv + String(data[j]) + '\n';
  return (csv);  
}

/* Self test function. 
 *  
 *  Ensures that the accelerometer is wired properly.  The accelerometer output for 
 *  each axis changes by a preset amount when the self test pin is activated.
 *  The sensor is tested by checking that the change is within parameters.
 *  A sensor status message is returned to the main program.
 *  
 */
String Self_test() {
  // initialize self test parameters for 12 bit resolution.
  short hi = 620;
  short lo = 186;
  short zhi = 1240;
  String message = "";                            
  // take neutral data reading        
  short X = analogRead(0);
  short Y = analogRead(1);
  short Z = analogRead(2);
  // Set pass parameters
  short xl = X - hi;
  short xh = X - lo;
  short yl = Y + lo;
  short yh = Y + hi;
  short zl = Z + lo;
  short zh = Z + zhi;
  digitalWrite(11, 1);                      // turn on self test pin
  delayMicroseconds(1000);                  // pause for sensor to adjust. 
  // take self test readings and check         
  X = analogRead(0);
  Y = analogRead(1);
  Z = analogRead(2);
  if (X > xl and X < xh){
    if (Y > yl and Y < yh){
      if (Z > zl and Z < zh){
        message = "Self test passed<br>";
        // show passing values for user reference.
        message = message + String(X)+' ' + String(Y)+ ' '+String(Z); 
      }
      else{
        message = "Self test failed Z";
      }
    }
    else{
      message = "Self test failed Y";  
    }
  }
  else{
    message = "Self test failed X";
  }
  digitalWrite(11, 0);                      // turn off self test pin
  return(message);
}
<<<<<<< HEAD
=======

>>>>>>> 70eb98ffa6e6d81118ded3bf2cc7e3403f7ac338
