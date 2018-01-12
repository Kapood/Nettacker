#!/usr/bin/env python
# -*- coding: utf-8 -*-


def all_messages():
    return \
        {
            "0": "Công cụ Nettacker bắt đầu ...\n\n",
            "1": "python nettacker.py [tuỳ chọn]",
            "2": "Hiển thị Menu Trợ giúp Nettacker",
            "3": "Vui lòng đọc giấy phép và thỏa thuận https://github.com/viraintel/OWASP-Nettacker\n",
            "4": "Động cơ",
            "5": "Tùy chọn đầu vào động cơ",
            "6": "chọn một ngôn ngữ {0}",
            "7": "quét tất cả các IP trong phạm vi",
            "8": "tìm và quét tên miền phụ",
            "9": "số chuỗi cho các kết nối đến máy chủ lưu trữ",
            "10": "số luồng cho máy chủ quét",
            "11": "lưu tất cả các bản ghi trong tệp (results.txt, results.html, results.json)",
            "12": "Mục tiêu",
            "13": "Tùy chọn nhập mục tiêu",
            "14": "mục tiêu (các) mục tiêu, tách biệt với \",\"",
            "15": "đọc (các) mục tiêu từ tệp",
            "16": "Tùy chọn phương pháp quét",
            "17": "chọn phương pháp quét {0}",
            "18": "chọn phương pháp quét để loại trừ {0}",
            "19": "(các) tên người dùng, tách biệt với \",\"",
            "20": "đọc (các) tên người dùng từ tệp",
            "21": "(các) danh sách mật khẩu, tách biệt với \",\"",
            "22": "đọc (các) mật khẩu từ tệp tin",
            "23": "(các) danh sách cổng, tách biệt với \",\"",
            "24": "đọc (các) mật khẩu từ tệp tin",
            "25": "thời gian để ngủ giữa mỗi yêu cầu",
            "26": "Không thể chỉ rõ mục tiêu (s)",
            "27": "Không thể chỉ rõ mục tiêu, không thể mở tệp: {0}",
            "28": "nó tốt hơn để sử dụng số thread thấp hơn 100, BTW chúng tôi đang tiếp tục ...",
            "29": "thiết lập thời gian chờ đến {0} giây, nó là quá lớn, phải không? bằng "
                  "cách chúng tôi đang tiếp tục ...",
            "30": "mô-đun quét này [{0}] không tìm thấy!",
            "31": "mô-đun quét này [{0}] không tìm thấy!",
            "32": "bạn không thể loại trừ tất cả các phương pháp quét",
            "33": "bạn không thể loại trừ tất cả các phương pháp quét",
            "34": "mô-đun {0} bạn đã chọn để loại trừ không tìm thấy!",
            "35": "nhập các phương thức đầu vào, ví dụ: \"ftp_brute_users = test, admin & "
                  "ftp_brute_passwds = read_from_file: /tmp/pass.txt&ftp_brute_port=21\"",
            "36": "không thể đọc tập tin {0}",
            "37": "Không thể chỉ định tên người dùng, không thể mở tệp: {0}",
            "38": "",
            "39": "Không thể chỉ định mật khẩu, không thể mở tệp: {0}",
            "40": "tập tin \"{0}\" không ghi được!",
            "41": "xin vui lòng chọn phương pháp quét của bạn!",
            "42": "loại bỏ các tập tin temp!",
            "43": "phân loại kết quả!",
            "44": "làm xong!",
            "45": "bắt đầu tấn công {0}, {1} của {2}",
            "46": "mô đun này \"{0}\" không có sẵn",
            "47": "tiếc là phiên bản này của phần mềm chỉ có thể chạy trên Linux/osx/windows.",
            "48": "Phiên bản Python của bạn không được hỗ trợ!",
            "49": "bỏ qua mục tiêu trùng lặp (một số tên miền phụ / tên miền có thể có cùng một IP và Ranges)",
            "50": "loại mục tiêu không xác định [{0}]",
            "51": "kiểm tra {0} phạm vi ...",
            "52": "kiểm tra {0} ...",
            "53": "HOST",
            "54": "USERNAME",
            "55": "MẬT KHẨU",
            "56": "HẢI CẢNG",
            "57": "KIỂU",
            "58": "SỰ MIÊU TẢ",
            "59": "chế độ tiết verbose (0-5) (mặc định 0)",
            "60": "hiển thị phiên bản phần mềm",
            "61": "kiểm tra cập nhật",
            "62": "",
            "63": "",
            "64": "Thử lại khi thời gian chờ kết nối (mặc định là 3)",
            "65": "kết nối ftp với {0}: {1} timeout, bỏ qua {2}: {3}",
            "66": "ĐĂNG KÝ THÀNH CÔNG!",
            "67": "ĐĂNG KÝ ĐÃ ĐƯỢC ĐƯỢC ĐƯỢC ĐƯỢC ĐƯỢC ĐƯỢC ĐƯỢC ĐƯỢC ĐƯỢC HƯỞNG CHO DANH BẠ!",
            "68": "kết nối ftp đến {0}: {1} không thành công, bỏ qua toàn bộ bước [process "
                  "{2} of {3}]! đi tới bước tiếp theo",
            "69": "mục tiêu đầu vào cho {0} mô-đun phải là DOMAIN, HTTP hoặc SINGLE_IPv4, bỏ qua {1}",
            "70": "user: {0} pass: {1} host: {2} port: {3} found!",
            "71": "(KHÔNG CẤP GIẤY PHÉP DANH SÁCH CÁC DANH SÁCH)",
            "72": "đang thử {0} {1} đang trong quá trình {2} của {3} {4}: {5}",
            "73": "kết nối smtp đến {0}: {1} timeout, bỏ qua {2}: {3}",
            "74": "kết nối smtp đến {0}: {1} không thành công, bỏ qua toàn bộ bước [process"
                  " {2} of {3}]! đi tới bước tiếp theo",
            "75": "mục tiêu đầu vào cho {0} mô-đun phải là HTTP, bỏ qua {1}",
            "76": "kết nối ssh đến {0}: {1} timeout, bỏ qua {2}: {3}",
            "77": "kết nối ssh tới {0}: {1} không thành công, bỏ qua toàn bộ bước [process {2} of"
                  " {3}]! đi tới bước tiếp theo",
            "78": "ssh kết nối đến% s:% s không thành công, bỏ qua toàn bộ bước [process% s of% s]! đi tới bước tiếp theo",
            "79": "OPEN PORT",
            "80": "host: {0} port: {1} found!",
            "81": "mục tiêu {0} đã gửi!",
            "82": "không thể mở tệp danh sách proxy: {0}",
            "83": "không thể tìm thấy tệp danh sách proxy: {0}",
            "84": "bạn đang chạy phiên bản OWASP Nettacker {0} {1} {2} {6} với tên mã {3} {4} {5}",
            "85": "tính năng này chưa có sẵn! hãy chạy \"git clone https://github.com/viraintel/OWASP-Nettacker.git\""
                  " hoặc \"pip install -U OWASP-Nettacker\" để có được phiên bản mới nhất.",
            "86": "xây dựng một đồ thị của tất cả các hoạt động và thông tin, bạn phải sử dụng"
                  " đầu ra HTML. biểu đồ khả dụng: {0}",
            "87": "để sử dụng biểu đồ tính năng tên tập tin đầu ra của bạn phải kết thúc bằng \".html\" hoặc \".htm\"!",
            "88": "xây dựng đồ thị ...",
            "89": "hoàn thành đồ thị xây dựng!",
            "90": "Đồ thị kiểm tra thâm nhập",
            "91": "Đồ thị này được tạo bởi OWASP Nettacker. Biểu đồ chứa tất cả các hoạt động mô-đun,"
                  " bản đồ mạng và thông tin nhạy cảm, Vui lòng không chia sẻ tệp này với bất kỳ ai "
                  "nếu nó không đáng tin cậy.",
            "92": "OWASP Nettacker Report",
            "93": "Chi tiết phần mềm: Phiên bản OWASP Nettacker {0} [{1}] trong {2}",
            "94": "không tìm thấy cổng mở!",
            "95": "không tìm thấy người dùng / mật khẩu!",
            "96": "Đã nạp {0} môđun ...",
            "97": "mô-đun đồ thị này không tìm thấy: {0}",
            "98": "mô-đun đồ thị này \"{0}\" không khả dụng",
            "99": "ping trước khi quét máy chủ",
            "100": "bỏ qua toàn bộ mục tiêu {0} và phương pháp quét {1} vì -ping-trước-scan là "
                   "đúng và nó đã không đáp ứng!",
            "101": "bạn không sử dụng phiên bản cuối cùng của OWASP Nettacker, vui lòng cập nhật.",
            "102": "không thể kiểm tra để cập nhật, vui lòng kiểm tra kết nối internet của bạn.",
            "103": "Bạn đang sử dụng phiên bản cuối cùng của OWASP Nettacker ...",
            "104": "danh sách thư mục được tìm thấy trong {0}",
            "105": "hãy chèn cổng thông qua các -g hoặc --methods-args chuyển đổi thay vì url",
            "106": "kết nối http {0} timeout!",
            "107": "",
            "108": "không tìm thấy thư mục hoặc tệp cho {0} trong cổng {1}",
            "109": "không thể mở được {0}",
            "110": "giá trị dir_scan_http_method phải là GET hoặc HEAD, được đặt mặc định là GET.",
            "111": "liệt kê tất cả các phương pháp args",
            "112": "không thể có được (0) mô-đun args",
            "113": "",
            "114": "",
            "115": "",
            "116": "",
            "117": ""
        }