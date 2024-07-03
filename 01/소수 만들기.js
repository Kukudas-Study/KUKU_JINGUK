function solution(nums) {
        let answer = 0;
        // 소수판별 함수
        function numnum(n) {
          // 2는 소수
          if (n === 2) return true;
          // 제곱근 까지만확인 (어떤 약수든 하나는 무조건 제곱근 이하)
          for (let i = 2; i <= Math.floor(Math.sqrt(n)); i++) {
            if (n % i === 0) return false;
          }
          return true;
        }
        // 3개 더하고
        for (let i = 0; i < nums.length - 2; i++) {
          for (let j = i + 1; j < nums.length - 1; j++) {
            for (let k = j + 1; k < nums.length; k++) {
              // 총합을 소수판별 함수로 트루면 ++
              let sum = nums[i] + nums[j] + nums[k];
              if (numnum(sum)) answer++;
            }
          }
        }
        return answer;
      }
