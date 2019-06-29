function setCookie(ck) {
    var Days = 30;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
    document.cookie = ck + ";expires=" + exp.toGMTString();
}

function getCookie(name) {
    var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
    if (arr = document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}


function login() {
    var username = document.getElementById("username");
    var pass = document.getElementById("password");
    if (username.value == "") {
        alert("请输入用户名");
    } else if (pass.value == "") {
        alert("请输入密码");
    }
    // data = post('localhost:15247/',{'username':username.value,'password':pass.value});
    rdata = $.ajax({
        type: 'POST',
        url: '/',
        data: {'username': username.value, 'password': pass.value},
        dataType: 'json',
        success: function (json) {
            if (json.status !== 200) {
                alert(json.data)
            } else {
                setCookie(json.cookie);
                window.location.href = '/html/index.html'
            }
        },
    });
    // dj = edata.json();
    // if (rdata.status !== 200) {
    //     alert(dj.data)
    // } else {
    //     setCookie(dj.cookie);
    //     window.location.href = './index.html'
    // }
}


function update_phone() {
    var phone = document.getElementById("phone");
    // var main_div = document.getElementById("main");
    var formData = new FormData($("#update")[0]);
    // formData.append('file', $('#phone')[0].files[0]);
    if (phone.files == null) {
        alert("请上传文件")
    } else {
        rdata = $.ajax({
            type: 'POST',
            url: '/home/phone',
            async: false,
            // cache: false,
            processData: false,
            // 告诉jQuery不要去设置Content-Type请求头
            contentType: false,
            beforeSend: function () {
                console.log("正在进行，请稍候");
            },
            data: formData,
            dataType: 'json',
            success: function (json) {
                if (json.status === 401){
                    alert(json.log);
                    window.location.href = '/html/login.html'
                }
                else if (json.status !== 200) {
                    alert(json.log)
                } else {
                    var ptext = '';
                    for (_index in json.log) {
                        ptext += "<p>"+json.log[_index]+"</p>"
                    }
                    ptext += "<a href=\"/csv/" + json['name'] + ".csv\">下载csv文件"+json['name']+"</a>";
                    // main_div.html(ptext);
                    $('#main').html(ptext);
                }
            },
        });
    }
}