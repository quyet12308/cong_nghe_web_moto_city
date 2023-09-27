let table = document.querySelector("#table")

function getDataFromServer(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        callback(response);
      }
    };
    xhr.open("GET", url, true);
    xhr.send();
  }
  
  // table.addEventListener("load",getDataFromServer("http://localhost:8001/api/get_data",(response)=>{
  //   console.log(response)
  //   console.log(typeof response)
  // }))

  table.addEventListener("load",()=>{
    console.log("get data ")
  })

  
//   // Sử dụng hàm để lấy dữ liệu từ máy chủ và xử lý kết quả
//   getDataFromServer("https://example.com/data", function(response) {
//     console.log(response);
//     // Xử lý dữ liệu nhận được từ máy chủ ở đây
//   });


//   var isDataLoaded = false;

// document.addEventListener("DOMContentLoaded", function() {
//   if (!isDataLoaded) {
//     getDataFromServer("http://localhost:8001/api/get_data", function(response) {
//       console.log(response);
//       // Xử lý dữ liệu nhận được từ máy chủ ở đây
      
//       isDataLoaded = true;
//     });
//   }
// });

// function getDataFromServerOnce() {
//     if (!isDataLoaded) {
//       getDataFromServer("http://localhost:8001/api/get_data", function(response) {
//         console.log(response);
//         // Xử lý dữ liệu nhận được từ máy chủ ở đây
        
//         isDataLoaded = true;
//       });
//     }
  
//     // Loại bỏ hàm xử lý sự kiện 'DOMContentLoaded' sau khi đã gọi hàm 'getDataFromServerOnce'
//     document.removeEventListener("DOMContentLoaded", getDataFromServerOnce);
//   }
  
//   document.addEventListener("DOMContentLoaded", getDataFromServerOnce);