// var data = [
//     [1, "Rider 1", "Country 1", "Points 1", "Leader 1", "Previous 1", "QAT 1", "INA 1", "ARG 1", "AME 1", "POR 1", "SPA 1", "FRA 1", "ITA 1", "CAT 1", "GER 1", "AUT 1", "RSM 1", "ARA 1", "JPN 1", "THA 1", "AUS 1", "MAL 1", "VAL 1"],
//     // [2, "Rider 2", "Country 2", "Points 2", "Leader 2", "Previous 2", "QAT 2", "INA 2", "ARG 2", "AME 2", "POR 2", "SPA 2", "FRA 2", "ITA 2", "CAT 2", "GER 2", "AUT 2", "RSM 2", "ARA 2", "JPN 2", "THA 2", "AUS 2", "MAL 2", "VAL 2"],
//     // [3, "Rider 3", "Country 3", "Points 3", "Leader 3", "Previous 3", "QAT 3", "INA 3", "ARG 3", "AME 3", "POR 3", "SPA 3", "FRA 3", "ITA 3", "CAT 3", "GER 3", "AUT 3", "RSM 3", "ARA 3", "JPN 3", "THA 3", "AUS 3", "MAL 3", "VAL 3"],
//     // [4, "Rider 4", "Country 4", "Points 4", "Leader 4", "Previous 4", "QAT 4", "INA 4", "ARG 4", "AME 4", "POR 4", "SPA 4", "FRA 4", "ITA 4", "CAT 4", "GER 4", "AUT 4", "RSM 4", "ARA 4", "JPN 4", "THA 4", "AUS 4", "MAL 4", "VAL 4"],
//     // [5, "Rider 5", "Country 5", "Points 5", "Leader 5", "Previous 5", "QAT 5", "INA 5", "ARG 5", "AME 5", "POR 5", "SPA 5", "FRA 5", "ITA 5", "CAT 5", "GER 5", "AUT 5", "RSM 5", "ARA 5", "JPN 5", "THA 5", "AUS 5", "MAL 5", "VAL 5"],
//     // [6, "Rider 6", "Country 6", "Points 6", "Leader 6", "Previous 6", "QAT 6", "INA 6", "ARG 6", "AME 6", "POR 6", "SPA 6", "FRA 6", "ITA 6", "CAT 6", "GER 6", "AUT 6", "RSM 6", "ARA 6", "JPN 6", "THA 6", "AUS 6", "MAL 6", "VAL 6"]
// ];

// var tableBody = document.getElementById('table-body');

// for (var i = 0; i < data.length; i++) {
//     var row = document.createElement('tr');

//     for (var j = 0; j < data[i].length; j++) {
//         var cell = document.createElement('td'); // Sử dụng 'td' cho tất cả các dòng
//         cell.textContent = data[i][j];
//         row.appendChild(cell);
//     }

//     tableBody.appendChild(row);
// }


function fetchDataFromServer() {
    // Tạo một đối tượng XMLHttpRequest
    var xhr = new XMLHttpRequest();
  
    // Định nghĩa hàm xử lý khi nhận được phản hồi từ máy chủ
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE) {
        if (xhr.status === 200) {
          // Phản hồi thành công, xử lý dữ liệu nhận được
          var response = JSON.parse(xhr.responseText);
          // Xử lý dữ liệu ở đây
          console.log(response);
        } else {
          // Xảy ra lỗi khi gửi yêu cầu đến máy chủ
          console.error('Lỗi khi gửi yêu cầu đến máy chủ');
        }
      }
    };
  
    // Thiết lập yêu cầu GET đến địa chỉ máy chủ
    xhr.open('GET', 'http://localhost:8001/api/get_data', true);
  
    // Gửi yêu cầu đến máy chủ
    xhr.send();
  }
  
  // Gọi hàm fetchDataFromServer khi trang web được tải
  window.onload = function() {
    fetchDataFromServer();
  };