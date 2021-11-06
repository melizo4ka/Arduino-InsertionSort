int A [500];
int value;
int randNumber;

void setup() {
  Serial.begin(9600);
  for(int k = 0; k < 500; k++){
    randNumber = random(500);
    A[k] = randNumber;
    }
}

void loop() {
  //insertionSort
  int key;
  int i;
    for (int j = 0; j < 500; j++){
        key = A[j];
        i = j - 1;
        while (i >= 0 and A[i] > key){
            A[i + 1] = A[i];
            i = i - 1;
            }
        A[i + 1] = key;
        }

  //returning array
  for(int i=0; i < 500; i++){
    value = A[i];
    Serial.println(value);
  }
}
