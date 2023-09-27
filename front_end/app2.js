let hasFetchedData = false;
let table = document.querySelector("#table")
var tableBody = document.getElementById('table-body');
let btn_check_3_lastest_time = document.querySelector("#check_3_lastest_time")
let time_show = document.querySelector("#time_show")
let add_more_rider = document.querySelector("#add_more_rider")
let edit_rider = document.querySelector("#edit_rider")


// Đợi cho trang web được tải hoàn toàn
document.addEventListener("DOMContentLoaded", function() {
    // Gọi hàm để lấy dữ liệu từ máy chủ nếu chưa lấy
    if (!hasFetchedData) {
        fetchDataFromServer();
        hasFetchedData = true; // Đã lấy dữ liệu, không gửi lại
    }

    add_more_rider.addEventListener("click",()=>{
        window.location.href = "add_more_rider.html"
    })

    edit_rider.addEventListener("click",()=>{
        window.location.href = "edit_rider.html"
    })

},false);

// Hàm để gửi yêu cầu đến máy chủ và xử lý dữ liệu trả về
function fetchDataFromServer() {
    // Sử dụng fetch hoặc XMLHttpRequest để gửi yêu cầu đến máy chủ
    fetch("http://localhost:8001/api/get_data")
        .then(response => response.json()) // Chuyển đổi dữ liệu trả về thành JSON
        .then(data => {
            // Xử lý dữ liệu ở đây
            // console.log( data);
            // console.log(typeof data)
            var datalist = JSON.parse(data)
            console.log(datalist)
            console.log(typeof datalist)
            for (var i = 0; i < datalist.length; i++) {
                var row = document.createElement('tr');
            
                for (var j = 0; j < datalist[i].length; j++) {
                    var cell = document.createElement('td'); // Sử dụng 'td' cho tất cả các dòng
                    cell.textContent = datalist[i][j];
                    row.appendChild(cell);
                }
            
                tableBody.appendChild(row);
            }
            // for (i in data){
            //     console.log(i)
            // }
        })
        .catch(error => {
            console.error("Lỗi khi gửi yêu cầu đến máy chủ:", error);
        });
}

// btn_check_3_lastest_time.addEventListener("click",()=>{
    
//     // time_show.classList.toggle("hidden")
//     fetch("http://localhost:8001/api/get_lastest_time")
//     .then(response => response.json())
//     .then(data => {
//         var datalist = JSON.parse(data);
//         console.log(datalist);
//         console.log(typeof datalist);
//         for (let value of datalist) {
//             time_show.innerHTML += `<p>truy cập lúc : ${value}</p>`;
//         }
//     })
//     .catch(error => {
//         console.error("Lỗi khi gửi yêu cầu đến máy chủ:", error);
//     });
// })

