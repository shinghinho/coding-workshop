//https://onecompiler.com/cpp/3ym8htx7w
#include <bits/stdc++.h>
using namespace std;
queue<string> q;
set<char>op;
set<char>num;
bool lex(string x){
    string t="";
    for(int i=0;i<x.length();i++){
        if(x[i]==' '){
          //q.push(t);
          //t="";
          continue;
        }
        if(op.find(x[i])!=op.end()){//is operator
            q.push(t);
            t=x[i];
            q.push(t);
            t="";
        }else if(isdigit(x[i])){//is number
            t+=x[i];
        }else{
          return 0;
        }
    }
    q.push(t);
    return 1;
}
bool is_num(string token){
  for(int i=0;i<token.length();i++){
    if(!isdigit(token[i])){
      return false;
    }
  }
  return true;
}
int precedence(string p){
  //cout<<"Ran function"<<endl;
	if(p=="+" or p=="-"){
		return 1;
	}else if(p=="*" or p=="/"){
		return 2;
	}
	return 999;
}
stack<string> parse(vector<string>g){//The shunting yard algorithm
	stack<string>ops;
	stack<string>output;
	for(int i=0;i<g.size();i++){
	  //cout<<g[i];
	  //cout<<endl;
	  string temp=g[i];
		if(is_num(g[i])){
			output.push(g[i]);
		}else if(g[i]=="+" or g[i]=="-" or g[i]=="*" or g[i]=="/"){
		  //cout<<precedence(ops.top())<<endl;
			while(!ops.empty() && ops.top()!="(" && precedence(ops.top()) >= precedence(temp)){
			  //cout<<"hi"<<g[i]<<endl;
			  string de=ops.top();
				output.push(de);
				ops.pop();
			}
			ops.push(temp);
		}else if(g[i]=="("){
			ops.push("(");
		}else if(g[i]==")"){
			while(ops.top()!="("){
				string temp=ops.top();
				output.push(temp);
				ops.pop();
			}
			ops.pop();
		}else{
		  cout<<"Impossible"<<endl;
		}
	}
	while(!ops.empty()){
		string temp=ops.top();
		output.push(temp);
		ops.pop();
	}
	return output;
}
double stod2(string gg){
  //cout<<gg<<endl;
  double answer=-1;
  double mult=1;
  for(int i=gg.length()-1;i>=0;i--){
    answer+=(gg[i]-'0')*mult;
    mult*=10;
  }
  //cout<<"Processing "<<gg;
  if(answer==-1){
    return answer;
  }
  return answer+1;
}
double evaluate(vector<string>x){
	vector<double>t;
	//cout<<999<<endl;
	/*for(int i=0;i<x.size();i++){
	  cout<<x[i];
	}*/
	//cout<<x.size()<<endl;
	for(int i=0;i<x.size();i++){
	  string abc=x[i];
		if(is_num(abc)){
		  //cout<<abc<<endl;
		  double c=stod2(abc);
		  if(stod2(abc)!=-1){
		    t.push_back(c);
		  }
		  //cout<<c<<endl;
		}else{
			double k2=t[t.size()-1];
			double k1=t[t.size()-2];
			t.pop_back();
			t.pop_back();
			if(x[i]=="+"){
				t.push_back(k1+k2);
			}else if(x[i]=="-"){
				t.push_back(k1-k2);
			}else if(x[i]=="*"){
				t.push_back(k1*k2);
			}else if(x[i]=="/"){
				t.push_back(k1/k2);
			}else{
			  cout<<"Impossible"<<endl;
			}
			/*for(int i=0;i<t.size();i++){
			  cout<<t[i]<<" ";
			}
			cout<<endl;*/
		}
	}
	//cout<<t.size()<<endl;
	return t[0];
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
    //initialization
    vector<string>v;
    if(lex(s)){
        while(q.size()){
          if(q.front()!=" "){
            v.push_back(q.front());
            q.pop();
          }
        }
        /*for(int i=0;i<v.size();i++){
            cout<<v[i]<<endl;
        }*/
     }else{
        cout<<"error"<<endl;
    }
    stack<string>test=parse(v);
    vector<string>tbk;
    //cout<<endl;
    while(!test.empty()){
      //cout<<test.top();
    	tbk.push_back(test.top());
    	test.pop();
	}
	reverse(tbk.begin(),tbk.end());
	cout<<evaluate(tbk);
  return 0;
}
