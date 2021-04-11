#include <iostream>
#include <string>
#include <string.h>
#include <regex>
#include <cmath>

using namespace std;

int main() {
  double R;
  double X;
  double Y;
  cin >> R >> X >> Y;

  // Target Point
  double TP;
  TP = sqrt(X*X + Y*Y);

  int sho = int(TP / R);

  if ( TP < R ) {
    cout << 2 << endl;
  } else if ( floor(TP / R) == (TP / R) ) {
    // warikireru
    cout << sho << endl;
  } else {
    // warikirenai
    cout << sho + 1 << endl;
  }
}
