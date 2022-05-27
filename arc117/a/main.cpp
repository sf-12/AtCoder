#include <iostream>
#include <string>
#include <string.h>
#include <regex>
#include <random>

using namespace std;

uint64_t get_rand_range( uint64_t min_val, uint64_t max_val ) {
    // 乱数生成器
    static mt19937_64 mt64(0);

    // [min_val, max_val] の一様分布整数 (int) の分布生成器
    uniform_int_distribution<uint64_t> get_rand_uni_int( min_val, max_val );

    // 乱数を生成
    return get_rand_uni_int(mt64);
}

int main() {
    int A;
    int B;
    cin >> A >> B;
    // cout << A << "and" << B << endl;

    int arr_length = A + B;

    // random_device rnd;
    // std::uniform_int_distribution<uint64_t> get_rand_uni_int( min_val, max_val );
    
    for (int i = 0; i < 10; ++i) {
      // cout << rnd() << endl;
      // cout << get_rand_uni_int(0,10**9) << endl;
      cout << get_rand_range(0,1000000001) << endl;

    }
    // while (1=1) {
      // make random plus value * A
      // make random minus value * B

      // sum is 0

    // }
}


