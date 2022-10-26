// calculator.cpp

#include <iostream>
#include <vector>

using namespace std;

int how_many_leading_digits(string s) {
    int i = 0;
    for (; i < s.length(); i++) {
        char c = s.at(i);
        if (!isdigit(c)) {
            return i;
        }
    }
    return i;
}

string leading_digits(string s) {
    int i = how_many_leading_digits(s);
    return s.substr(0, i);
}

vector<string> lex(string s) {
    int i = 0;
    vector<string> ts = vector<string>();
    while (i < s.length()) {
        char c = s.at(i);
        if (isdigit(c)) {
            string digits = leading_digits(s.substr(i));
            ts.push_back(digits);
            i += digits.length();
        } else {
            i++;
            if (c == ' ') {
                continue;
            } else if (c == '(' || c == ')' || c == '+' || c == '*' || c == '-' || c == '/') {
                ts.push_back(string(1, c));
            } else {
                cout << "Error: unexpected character, " << c << endl;
                exit(-1);
            }
        }
    }
    return ts;
}

vector<string> parse(vector<string> tokens) {
    // TODO: Implement this using the shunting yard algorithm.
    return vector<string>();
}

int evaluate(vector<string> ast) {
    // TODO: How should we evaluate reverse Polish notation?
    return 27102022;
}

int main() {
    string user_input;
    cout << "Input: ";
    getline(cin, user_input);
    vector<string> ts = lex(user_input);
    vector<string> ast = parse(ts);
    int result = evaluate(ast);
    cout << result << endl;
    return 0;
}
