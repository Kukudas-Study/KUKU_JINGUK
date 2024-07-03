function solution(bridge_length, weight, truck_weights)
        let time_answer = 0;
        // 다리길이만큼 배열 만들고 0으로 채움
        let bridge = new Array(bridge_length).fill(0);
        // 무게의 합
        let weight_sum = 0;
        // 남은 트럭이 없을때까지 반복
        while (truck_weights.length) {
          time_answer++; 
          // 다리를 나가면 무게 총합에서 나간 트럭의 무게 뺴줌
          weight_sum -= bridge.shift(); // 6
          // weight 보다 총합이 높으면 0  
          if (weight_sum + truck_weights[0] > weight) {
            bridge.push(0);
            // 아니면 truck
          } else {
            const truck = truck_weights.shift();
            bridge.push(truck);
            weight_sum += truck;
          }
        }
        // 위에트럭이 지나가는 시간을 다리길이만큼 더해줌
        time_answer += bridge_length;

        return time_answer;
      }
