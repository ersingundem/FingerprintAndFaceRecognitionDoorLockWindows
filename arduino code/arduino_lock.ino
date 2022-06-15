char read;
String reads="";
String command;
const int RELAY_PIN = 4;
const int RELAY_PIN1 = 5;


void setup() {  
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(RELAY_PIN1, OUTPUT);
}

void loop() {  
  command = lerSerial();  
  if (command.length()>0) {
    Serial.print(command);
    if (command == "1"){
      digitalWrite(13, HIGH);
      digitalWrite(RELAY_PIN, HIGH);
      delay(50);
      digitalWrite(13, LOW);
      digitalWrite(RELAY_PIN, LOW);
    }
    
    if (command == "2") {
      digitalWrite(13, HIGH);
      digitalWrite(RELAY_PIN1, HIGH);
      delay(50);
      digitalWrite(13, LOW);
      digitalWrite(RELAY_PIN1, LOW);
     
    }
   
   
  }
}

String lerSerial(){
  reads ="";
  read=' ';
  while(Serial.available()>0){
    read = (byte)Serial.read();
    reads += read;
    read = ' ';
    delay(10);    
  }  
  return reads;
}
