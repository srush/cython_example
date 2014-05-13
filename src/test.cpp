#include "test.h"
#include <vector>
using namespace std;

int run(vector<int> args) {
    int sum = 0;
    for (int i = 0; i < args.size(); ++i) {
        sum += args[i];
    }
    return sum;
}
