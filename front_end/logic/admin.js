url_get_the_name_of_the_race = "http://localhost:8001/api/get_the_name_of_the_race"
url_update_the_point_of_the_race = "http://localhost:8001/api/update_the_point_of_the_race"

document.addEventListener("DOMContentLoaded", async function() {

    empty_column = await get_data_from_server(url_get_the_name_of_the_race)
    // alert(empty_column)
    let sub_content_header = document.querySelector("#sub_content_header")
    sub_content_header.innerHTML = `
    <h1>${empty_column} round</h1>
    `
    let names = [
      "BAGNAIA Francesco",
      "QUARTARARO Fabio",
      "BASTIANINI Enea",
      "ESPARGARO Aleix",
      "MILLER Jack",
      "BINDER Brad",
      "RINS Alex",
      "ZARCO Johann",
      "MARTIN Jorge",
      "OLIVEIRA Miguel",
      "VINALES Maverick"
  ]
  
  let countrys = [
  "ITA","FRA","ITA","SPA","AUS","RSA","SPA","FRA","SPA","POR","SPA"
  ]
    let table_body_admin_page = document.querySelector("#table_body_admin_page")
    for(let i = 0 ; i < 11 ; i++){
      // console.log(i)
      table_body_admin_page.innerHTML += `
      <tr>
      <td class="center">${names[i]} </td>
      <td class="center">${countrys[i]}</td>
      <td>
        <select name="point${i+1}" onchange="validatePoints(this)">
          <option value="">Chọn điểm</option>
          <option value="25">Vị trí thứ nhất - 25 điểm</option>
          <option value="20">Vị trí thứ hai - 20 điểm</option>
          <option value="16">Vị trí thứ ba - 16 điểm</option>
          <option value="13">Vị trí thứ tư - 13 điểm</option>
          <option value="11">Vị trí thứ năm - 11 điểm</option>
          <option value="10">Vị trí thứ sáu - 10 điểm</option>
          <option value="9">Vị trí thứ bảy - 9 điểm</option>
          <option value="8">Vị trí thứ tám - 8 điểm</option>
          <option value="7">Vị trí thứ chín - 7 điểm</option>
          <option value="6">Vị trí thứ mười - 6 điểm</option>
          <option value="5">Vị trí thứ mười một - 5 điểm</option>
          
        </select>
      </td>
    </tr>
      `
    }
    
    let btn = document.querySelector("#btn")
    btn.addEventListener("click",async ()=>{
    // var inputs = document.querySelectorAll('table input');
    // var values = [];

    // inputs.forEach(function(input) {
    //   values.push(input.value);
    // });

    var selects = document.getElementsByTagName('select');
  var selectedValues = [];

  for (var i = 0; i < selects.length; i++) {
    var select = selects[i];
    var selectedValue = select.value;

    // if (selectedValue !== "") {
    //   selectedValues.push(selectedValue);
    // }
    selectedValues.push(selectedValue);
  }

  // var selectedValuesDiv = document.getElementById('selectedValues');
  // selectedValuesDiv.innerHTML = "Các giá trị đã chọn: " + selectedValues.join(", ");
  
  console.log(selectedValues.join(", "))
  console.log( selectedValues)
  console.log(typeof selectedValues)
  // let list_data = selectedValues.values
  let list_data =  Object.values(selectedValues)
  console.log( `list data = ${list_data}`)
  console.log(typeof list_data)

  data = {
    arr_data:list_data,
    empty_column:empty_column
}
a = await send_data_to_server_admin_basic(data);
alert(a)
}

    // console.log(values);
    // data = {
    //     arr_data:values,
    //     empty_column:empty_column
    // }
    // a = await send_data_to_server_admin_basic(data);
    // alert(a)
  // }
  ) ;
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

  function validatePoints(select) {
    var selectedValue = select.value;
  
    // Kiểm tra giá trị đã được chọn và ngăn chọn hai tùy chọn giống nhau
    var selects = document.getElementsByTagName('select');
    for (var i = 0; i < selects.length; i++) {
      if (selects[i] !== select && selects[i].value === selectedValue) {
        selects[i].value = "";
      }
    }
  }