#include <iostream>
#include <string>
#include <string.h>
#include <regex>

using namespace std;

int main() {
  int N;
  cin >> N;
  string str = to_string(N);
  string new_str = "";
  bool parind_flag = true;
  bool all_zero_flag = true;


  // for all 0
  for ( int t = str.length() - 1; t >= 0; t--) {
    char numt = str[t];
    if (numt != '0') {
      all_zero_flag = false;
      break;
    }
  }

  if (all_zero_flag) {
    cout << "Yes" << endl;
    return 0;
  }

  // removde 0
  for ( int i = str.length() - 1; i >= 0; i--) {
    char num = str[i];
    if (num == '0') {
      str.pop_back();;
    } else {
      break;
    }
  }
  // cout << str << endl;

  for (int s = 0; s < int(str.length()/2); s++) {
    int back_num = str.length() -1 - s;
    // cout << "back_num " << back_num << endl;
    // cout << "new_str[s] " << new_str[s] << endl;
    // cout << "new_str[back_num] " << new_str[back_num] << endl;
    if (str[s] != str[back_num]) {
      parind_flag = false;
      break;
    }
  }

  if (parind_flag) {
    cout << "Yes" << endl;
  } else {
    cout << "No" << endl;
  }
}
