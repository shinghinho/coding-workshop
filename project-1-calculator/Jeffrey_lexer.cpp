#include <bits/stdc++.h>
using namespace std;
queue<string> q;
set<char>op;
set<char>num;
bool lex(string x){
    string t="";
    for(int i=0;i<x.length();i++){
        if(x[i]==' '){
          q.push(t);
          t="";
          continue;
        }
        if(op.find(x[i])!=op.end()){//is operator
            q.push(t);
            t="";
            t=x[i];
            q.push(t);
            t="";
        }else if(num.find(x[i])!=num.end()){//is number
            t+=x[i];
        }else{
          return 0;
        }
    }
    q.push(t);
    return 1;
}
int main(){
    string s;
    for(int i=0;i<=9;i++){
        string temp=to_string(i);
        num.insert(temp[0]);
    }
    op.insert('(');
    op.insert(')');
    op.insert('+');
    op.insert('-');
    op.insert('*');
    op.insert('/');
    getline(cin,s);
    getline(cin,s);
    vector<string>v;
    if(lex(s)){
        while(q.size()){
          v.push_back(q.front());
          q.pop();
        }
        for(int i=0;i<v.size();i++){
            cout<<v[i]<<endl;
        }
     }else{
        cout<<"error"<<endl;
    }
    return 0;
}
