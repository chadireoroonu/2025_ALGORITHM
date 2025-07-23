// 추억 점수
// https://school.programmers.co.kr/learn/courses/30/lessons/176963

#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer(photo.size(), 0);
    map<string, int> score;
    
    for (int i = 0; i < name.size(); i++) {
        score[name[i]] = yearning[i];
    }
    
    for (int i = 0; i < photo.size(); i++) {
        for (const string& person : photo[i]) {
            auto n = score.find(person);
            if (n != score.end()) {
                answer[i] += n -> second;
            }
        }
    }
    
    return answer;
}

// #include <string>
// #include <vector>
// #include <map>

// using namespace std;

// vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
//     vector<int> answer(photo.size(), 0);
//     map<string, int> score;
    
//     for (int i = 0; i < name.size(); i++) { // 그리운 사람의 그리움 점수 묶기
//         score[name[i]] = yearning[i];
//     }
    
//     for (int i = 0; i < photo.size(); i++) { // 각 사진
//         for (int j = 0; j < photo[i].size(); j++) { // 사진 한 장 속 각 인물
//             if (score.count(photo[i][j])) { // 그리운 사람인지 확인
//                 answer[i] += score.at(photo[i][j]); // 그리움 점수 더하기
//             }
//         }
//     }
    
//     return answer;
// }