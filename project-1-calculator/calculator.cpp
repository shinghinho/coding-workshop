// calculator.cpp

#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <string>

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

bool is_num(string token) {
    for (int i = 0; i < token.length(); i++) {
        if (!isdigit(token.at(i))) return false;
    }
    return true;
}

bool is_operator(string token) {
    return token == "+" || token == "-"
        || token == "*" || token == "/";
}

bool is_lparen(string t) {
    return t == "(";
}

bool is_rparen(string t) {
    return t == ")";
}

int precedence(string op) {
    if (op == "+" || op  == "-") {
        return 1;
    } else if (op == "*" || op == "/") {
        return 2;
    } else {
        cout << "Impossible" << endl;
        exit(-1);
    }
}

queue<string> parse(vector<string> tokens) {
    // TODO: Implement this using the shunting yard algorithm.
    stack<string> ops = stack<string>();
    queue<string> output = queue<string>();
    for (int i = 0; i < tokens.size(); i++) {
        string t = tokens.at(i);
        if (is_num(t)) {
            output.push(t);
        } else if (is_operator(t)) {
            while (!ops.empty() && !is_lparen(ops.top()) && precedence(ops.top()) >= precedence(t)) {
                string e = ops.top();
                ops.pop();
                output.push(e);
            }
            ops.push(t);
        } else if (is_lparen(t)) {
            ops.push(t);
        } else if (is_rparen(t)) {
            while (!is_lparen(ops.top())) {
                string e = ops.top();
                ops.pop();
                output.push(e);
            }
        }
    }
    while (!ops.empty()) {
        string e = ops.top();
        ops.pop();
        output.push(e);
    }
    return output;
}

double apply(string op, double a, double b) {
    if (op == "+") return a+b;
    else if (op == "-") return a-b;
    else if (op == "*") return a*b;
    else if (op == "/") return a/b;
    cout << "Impossible: unknown operator" << endl;
    exit(-1);
}

double evaluate(queue<string> ast) {
    stack<double> buffer = stack<double>();
    while (!ast.empty()) {
        string t = ast.front();
        ast.pop();
        if (is_num(t)) {
            buffer.push(stod(t, nullptr));
        } else if (is_operator(t)) {
            double b = buffer.top();
            buffer.pop();
            double a = buffer.top();
            buffer.pop();
            double c = apply(t, a, b);
            buffer.push(c);
        }
    }
    return buffer.top();
}

int main() {
    string user_input;
    cout << "Input: ";
    getline(cin, user_input);
    vector<string> ts = lex(user_input);
    queue<string> ast = parse(ts);
    double result = evaluate(ast);
    cout << result << endl;
    return 0;
}
