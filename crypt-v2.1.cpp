#include <iostream>
#include <string>
#include <vector>
#include <cmath> 
#include <print>
#include <numeric>
#include <algorithm>

bool DBUG=false;
bool DBUG_V=false;


string numStr = "";
vector<int> numDist; // number distribution (# of occurances)
vector<float> numPerc; // number distribution (% of occurances)
float val = 0.0;

using namespace std;

int ranNum(int dLen=64){
    'LockBox-Crypt (CSRNG) v2.1\n\nGenerates a secure random integer of a specified length.';

    // generate number 
    // number formula in PYTHON version:
    // temp = ((pu.cpu_stats().ctx_switches * int(time()*1000)) % 100000)*(pu.virtual_memory().available % 100000) * 3.1459265; temp = round(temp); temp = (temp:=temp*(pu.cpu_stats().interrupts % 100000)) % 1000000007
    int temp = 0;
    // genGoesHere

    // convert to string and trim to dLen
    numStr = to_string(temp);
    while(numStr.length() != dLen){
        if(numStr.length() < dLen){
            temp = temp*2;
            numStr = to_string(temp);
        } else if(numStr.length() > dLen){
            numStr = numStr.substr(0, dLen);
        }
    }

    return temp;
};

void ranNumST(int dLen=128, int itCount=1000, float tlrnc=2){
    'LockBox-Crypt (CSRNG) v2.1\n\nTests the cryptographic security of LockBox-Crypt by analyzing patterns of multiple iterations of the function.';

    // add test numbers to numArray
    vector<int> numArray;
    for(int i=0; i<itCount; i++){
        numArray.push_back(ranNum(dLen));
    } 

    // get number distribution
    for(int i=0; i<itCount; i++){
        int occ=0;
        for(int j=0; j<itCount; j++){
            if(numArray[i] == numArray[j]){occ++;};
        }
    }

    // get distribution percentages
    for(int i=0; i<numDist.size(); i++){
        numPerc.pushback(round((numDist[i]/itCount)*100)/100); // round to 2 decimal places
    }

    // num dist info
    if(DBUG){
        cout << "DBUG:NumTests()::SelRunArray:[numarray] | runModeLanguage:UNI/CPP";
        cout << "\nNumber Distribution (i): " << numDist << " | ChkSm-" << (accumulate(numDist.begin(), numDist.end(), 0)) << "/" << (dLen*itCount) << endl;
        cout << "\nNumber Distribution (%): " << numPerc << endl;
        // 3 most commonly occuring numbers
        vector<int> top3;
        for(int i=0; i<3; i++){
            int maxIndex = distance(numDist.begin(), max_element(numDist.begin(), numDist.end()));
            top3.pushback(numArray[maxIndex]);
            numDist[maxIndex] = -1; // mark as used
        }

        // 3 least commonly occuring numbers
        vector<int> least3;
        for(int i=0; i<3; i++){
            int minIndex = distance(numDist.begin(), min_element(numDist.begin(), numDist.end()));
            least3.pushback(numArray[minIndex]);
            numDist[minIndex] = 999999999; // mark as used
        }
        cout << "\n3 Most Commonly Occuring Numbers: " << top3 << endl;
        cout << "\n3 Least Commonly Occuring Numbers: " << least3 << endl;

        // numeric consistency / tolerance check
        // this check is to see if any distribution percentage exceeds the tolerance percentage- if it fails, on top of printing a FAIL instead of PASS, print out the percentage of occurances, the percentage difference, and the tolerance range
        // python code version
        /*
        tollvl = (tlrnc/100)*(itCount*dLen/10)
        print(f"TLRNC LVL: {tollvl} ({tlrnc}%)")
        for idx, val in enumerate(numPerc):
            if(DBUG_V): input(f"NumPerc[].indexDigit(): {val} | {tlrnc+10}/{10-tlrnc} | {val}")
            if val < (10-tlrnc) or val > (10+tlrnc):
                print(f"DGT{idx}        | TLRNCE..........{CRED+'FAIL'+CEND} | {val} / {round(val-(10+tlrnc), 2) if (val > (10+tlrnc)) else round((10-tlrnc)-val, 2)}%; {10+tlrnc}/{10-tlrnc}")
            else:
                print(f"DGT{idx}        | TLRNCE..........{CGRE+'PASS'+CEND}")
        print(f"Number Distribution: {numPerc}")
        
        */
        float tollvl = (tlrnc/100)*(itCount*dLen/10);
        cout << "\nTolerance Level: " << tollvl << "(" << tlrnc << "%)" << endl;
        for(int i=0; numPerc<i; i++){
            val = numPerc[i];
            if(DBUG_V){cout << "NumPerc[].indexDigit(): " << val << " | " << tlrnc+10 << "/" << tlrnc-10 << " | " << val};
            if(numPerc[i] < (10-tlrnc) || numPerc[i] > (10+tlrnc)){
                cout << "DGT" << i << "   TLRNCE........FAIL | " << val << "/" << if(val>(10+tlrnc)){(round((val-(10+tlrnc)*100)/100))} else{(round(((10-tlrnc)-val)*100)/100)} << "%; " << 10+tlrnc << "/" << 10-tlrnc << endl;
            } else {
                cout << "DGT" << i << "   TLRNCE........PASS" << endl;
            }
            cout << "Number Distribution: " << numPerc << endl;
        }
    }
}