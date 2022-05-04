#include <iostream>
#include <opencv2/opencv.hpp>
#include <bitset>
#include <vector>
#include <windows.h>

using namespace std;

std::vector<string> LFSR(int pixels){
    const int size = 160;
    //initialise seed
    std::bitset<size> current;
    current[0] = 1;
    current[10] = 1;
    current[16] = 1;
    current[32] = 1;
    current[37] = 1;
    current[54] = 1;
    current[58] = 1;
    current[69] = 1;
    current[73] = 1;
    current[88] = 1;
    current[96] = 1;
    current[100] = 1;
    current[111] = 1;
    current[127] = 1;
    current[140] = 1;
    current[146] = 1;
    current[157] = 1;
    current[159] = 1;

    std::bitset<size> original;
    original = current;
    vector<string> vec;
    string currentOutput = "";
    int count = 0;

    while (true){
        //saves output bit
        currentOutput = currentOutput + to_string(current[0]);
        
        if (currentOutput.length() == 8){
            vec.push_back(currentOutput);
            count = count + 1;
            currentOutput = "";
        };

        //set taps
        int newbit = (current[0] ^ current[30] ^current[56] ^current[101]) & 1;
        current = current >> 1;
        current[size - 1] = newbit;

        //checks if LFSR is repeating itself
        if (current == original || count == (pixels + 1)){
            break;
        };
    };

    return vec;
}

int main(){

    cv::Mat imageMat;
    //read image
    imageMat = cv::imread("C:/Users/khool/Desktop/FYP/2703LFSR/test images/peppers.tif", 0);

    std::vector<unsigned char> pixel;

    int arrayLength = imageMat.cols * imageMat.rows;

    //save pixel values
    for(int c = 0; c < imageMat.cols; ++c){
        for(int r = 0; r < imageMat.rows; ++r) {
        pixel.push_back((unsigned char)imageMat.at<uchar>(c,r));
        };
    };

    unsigned char* msg = new unsigned char[arrayLength];
    for(int i = 0; i < arrayLength; i++){
        msg[i] = pixel.at(i);
    };
    
    vector<string> vec;
    vec = LFSR(arrayLength);

    for (int i=0; i<vec.size(); i++){
        int temp = std::stol(vec.at(i),nullptr,2);
        unsigned char temp2 = (unsigned char)temp;
        msg[i] ^= temp2;
    };
    

    cv::Mat encrypted = cv::Mat(imageMat.cols,imageMat.rows, CV_8UC1, msg);
    cv::imshow("encrypted",encrypted);
    cv::imwrite("C:/Users/khool/Desktop/FYP/2703LFSR/peppers_lfsr.png",encrypted);
    cv::waitKey(0);

    return 0;
    
}
