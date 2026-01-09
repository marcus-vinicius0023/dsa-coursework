#include <stdio.h>
#include <string.h> 

char* invert_string(char* str);
char* reverse_words(char* str);

int main(){

    char string[33] = "yellow cow eating a grass!";
    
    printf("%s\n",reverse_words(string));

}

char* invert_string(char* str){
    //The algorithm starts by initializing two pointers: one at the beginning of the string and the other at the end. 
    // In each iteration, they swap values. After the swap, the 'start' pointer is incremented and the 'end' pointer is decremented. 
    // When the pointers meet, the string is fully inverted.

    if (str == NULL || *str == '\0') return str;

    int start = 0; 
    int end = strlen(str) - 1;

    while (start < end){
        
        char tmp_start = str[start];
        str[start] = str[end]; 
        str[end] = tmp_start;
        start++;
        end--;
    }
    return str;
}
    
char* reverse_words(char* str){
    //  This function performs an in-place word reversal within a string. It iterates through the character array using two 
    //pointers to identify word boundaries. When a space or the null terminator is encountered, it reverses the characters of 
    //the identified word by swapping them from the outside in. The algorithm maintains the original word order and spacing while 
    //achieving O(N) time complexity and O(1) space complexity.

    if (str == NULL || *str == '\0') return str;

    int left = 0;
    int right = 0;
    
    int len = strlen(str);

    while (left < len){
        // Reverse if find a ' ' or is a end of string.
        if (str[right] == ' ' || str[right] == '\0'){
            int end_word = right;
            right--;
            while (left < right){
                char tmp_start = str[left];
                str[left] = str[right];
                str[right] = tmp_start; 
                left++;
                right--;
            }
            right = end_word;
            if (str[right] == '\0') return str;

            while (str[right] == ' '){
                right++;
                if (str[right] == '\0') return str;
            }
            left = right;
        }
        else{
            right++;
        }
    }
    return str;
}



