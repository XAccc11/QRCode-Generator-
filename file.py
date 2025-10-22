import qrcode
upi_id = input("Enter UPI ID: ")


phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'
Paytm_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'
Google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'


phonepe_qr = qrcode.make(phonepe_url)
Paytm_qr = qrcode.make(Paytm_url)
Google_pay_qr = qrcode.make(Google_pay_url)

phonepe_qr.save("phonepe_qr.png")
Paytm_qr.save("Paytm_qr.png")
Google_pay_qr.save("Google_pay_qr.png")

phonepe_qr.show()
Paytm_qr.show()
Google_pay_qr.show()