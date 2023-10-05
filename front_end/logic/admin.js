url_get_the_name_of_the_race = "http://localhost:8001/api/get_the_name_of_the_race"
url_update_the_point_of_the_race = "http://localhost:8001/api/update_the_point_of_the_race"

document.addEventListener("DOMContentLoaded", async function() {

    empty_column = await get_data_from_server(url_get_the_name_of_the_race)
    // alert(empty_column)
    let sub_content_header = document.querySelector("#sub_content_header")
    sub_content_header.innerHTML = `
    <h1>${empty_column} round</h1>
    `

    let table_body_admin_page = document.querySelector("#table_body_admin_page")
    let btn = document.querySelector("#btn")
  btn.addEventListener("click",async ()=>{
    var inputs = document.querySelectorAll('table input');
    var values = [];

    inputs.forEach(function(input) {
      values.push(input.value);
    });
    // console.log(values);
    data = {
        arr_data:values,
        empty_column:empty_column,
    }
    a = await send_data_to_server_admin_basic(data);
    alert(a)
  }) ;
});

let send_data_to_server_admin_basic = async (data) => {
  
    // Tạo các tùy chọn cho yêu cầu POST
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data) 
    };
  
    // Gửi yêu cầu POST đến backend
    return fetch(url_update_the_point_of_the_race, requestOptions)
      .then(response => response.text())
      .then(data => {
        // Xử lý kết quả trả về từ server
        try {
          const parsedData = JSON.parse(data);
          a = parsedData.response;
          console.log(a);
          console.log(typeof(a))
          
          return a


          // Thực hiện các xử lý khác với dữ liệu ở đây
        } catch (error) {
          console.error("Lỗi khi phân tích dữ liệu JSON: ", error);
        }
      })
      .catch(error => {
        console.error("Lỗi khi gửi yêu cầu: ", error);
      });
  };

  let get_data_from_server = async (url) => {
    try {
      const response = await fetch(url);
      const data = await response.json();
      console.log(data);
      console.log(typeof data);
      return data.response;
    } catch (error) {
      console.error("Lỗi khi gửi yêu cầu đến máy chủ:", error);
      throw error;
    }
  };