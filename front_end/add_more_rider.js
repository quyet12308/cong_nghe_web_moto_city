// Lắng nghe sự kiện khi form được gửi đi
document.getElementById("myForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Ngăn chặn gửi form mặc định

    // Lấy giá trị từ các trường nhập liệu
    // let riderName = document.getElementById('rider_name').value;
    // Lấy giá trị từ các trường nhập liệu khác
    let myForm = document.querySelector("#myForm")
    let rider_name  = document.getElementById('rider_name ').value;
    let country  = document.getElementById('country ').value;
    let QAT = document.getElementById('QAT').value || null;
    let  INA = document.getElementById(' INA').value || null;
    let  ARG = document.getElementById(' ARG').value || null;
    let  AME = document.getElementById(' AME').value || null;
    let  POR = document.getElementById(' POR').value || null;
    let  SPA  = document.getElementById(' SPA ').value || null;
    let FRA  = document.getElementById('FRA ').value || null;
    let ITA  = document.getElementById('ITA ').value || null;
    let CAT = document.getElementById('CAT').value || null;
    let  GER = document.getElementById(' GER').value || null;
    let  NED = document.getElementById(' NED').value || null;
    let  GBR = document.getElementById(' GBR').value || null;
    let  AUT = document.getElementById(' AUT').value || null;
    let  RSM = document.getElementById(' RSM').value || null;
    let  ARA = document.getElementById(' ARA').value || null;
    let  JPN  = document.getElementById(' JPN ').value || null;
    let THA  = document.getElementById('THA ').value || null;
    let AUS = document.getElementById('AUS').value || null;
    let  MAL = document.getElementById(' MAL').value || null;
    let  VAL = document.getElementById(' VAL').value || null;

    data_ = [ QAT, INA, ARG, AME, POR, SPA ,FRA ,ITA ,CAT, GER, NED, GBR, AUT, RSM, ARA, JPN ,THA ,AUS, MAL, VAL]
    
    // Kiểm tra các giá trị nhập liệu
    var isValid = true;

    if (rider_name === "") {
      isValid = false;
      alert("Vui lòng nhập tên tay đua.");
    }
    if (country === "") {
      isValid = false;
      alert("Vui lòng nhập đất nước của tay đua.");
    }
    // Kiểm tra các trường nhập liệu khác

    for(let i in data_){
      console.log(i)
    }
    // Gửi dữ liệu đến server nếu hợp lệ
    if (isValid) {
      let data = {
        rider_name :rider_name ,
        country :country ,
        QAT:QAT,
        INA: INA,
        ARG: ARG,
        AME: AME,
        POR: POR,
        SPA : SPA ,
        FRA :FRA ,
        ITA :ITA ,
        CAT:CAT,
        GER: GER,
        NED: NED,
        GBR: GBR,
        AUT: AUT,
        RSM: RSM,
        ARA: ARA,
        JPN : JPN ,
        THA :THA ,
        AUS:AUS,
        MAL: MAL,
        VAL: VAL
      }
      console.log(data)


      data_cover = createDataObject(data)
      console.log(data_cover)
      // a = send_data_to_server_for_add_rider(data_cover)
      // Gửi dữ liệu đến server, ví dụ:
      // var data = { riderName: riderName, ... };
      // fetch('/submit_form', {
      //   method: 'POST',
      //   headers: {
      //     'Content-Type': 'application/json'
      //   },
      //   body: JSON.stringify(data)
      // })
      // .then(response => response.json())
      // .then(data => {
      //   // Xử lý phản hồi từ server
      // })
      // .catch(error => {
      //   // Xử lý lỗi
      // });

      // Hoặc có thể sử dụng XMLHttpRequest hoặc thư viện AJAX khác để gửi dữ liệu đến server
    }
  });
  function createDataObject(data) {

    return JSON.stringify(data);
  }

  let send_data_to_server_for_add_rider = async (data) => {
    // Ngăn chặn hành vi mặc định của form submit
    // event.preventDefault();
  
    // Tạo các tùy chọn cho yêu cầu POST
    const requestOptions = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: data 
    };
  
    // Gửi yêu cầu POST đến backend
    return fetch(url_login_basic, requestOptions)
      .then(response => response.text())
      .then(data => {
        // Xử lý kết quả trả về từ server
        try {
          const parsedData = JSON.parse(data);
          a = parsedData.response;
          console.log(a);
          console.log(typeof(a))
          console.log(a.message)
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