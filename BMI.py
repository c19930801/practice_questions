import tkinter as tk
# 建立主視窗
window =tk.Tk()
# 設定主視窗大小
window.geometry("800x600")
# 設定主視窗標題
window.title("圖形化範例-BMI測量")
# 需要主視窗建立後才可建立，否則會報錯
return_msg = tk.StringVar() # BMI 回傳值 #預設值為空字串
height_msg = tk.IntVar() # 身高 #資料型態為「整數
weight_msg = tk.IntVar() # 體重
# 設定身高 標籤 
height_label = tk.Label(window, text="請輸入身高:", foreground="red", font=("標楷體", 12), padx=30, pady=20)
height_label.pack()
# 設定身高 輸入框
height_entry = tk.Entry(window, foreground="green", textvariable=height_msg)
height_entry.pack()
# 設定 體重標籤l
weight_label = tk.Label(window, text="請輸入體重:", foreground="red", font=("標楷體", 12), padx=30, pady=20)
weight_label.pack()
# 設定 體重輸入框
weight_entry = tk.Entry(window, foreground="green", textvariable=weight_msg)
weight_entry.pack()
# 設定回應值 標籤
returnMsg_label = tk.Label(window, textvariable=return_msg, foreground="red", font=("標楷體", 12), padx=30, pady=20)
returnMsg_label.pack()
def BMI():
    # BMI 計算，四捨五入取到小數第二位
    BMI_value = round(weight_msg.get() / ((height_msg.get() / 100) ** 2),2) 
    #回傳結果，設定 return_msg 數值及評語
    return_msg.set("BMI 計算後數值 = " + str(BMI_value) + "\n" + BMI_Status(BMI_value))
# 透過 BMI 指數，回傳相對應評語
def BMI_Status(BMI_value):

    
    if BMI_value < 18.5:
        return "BMI 過低，體重過輕"
    elif BMI_value < 24:
        return "BMI 正常，標準體位"
    else:
        if BMI_value < 27:
            return "BMI 過高，體重過重"
        elif BMI_value < 30:
            return "BMI 過高，輕度肥胖"
        elif BMI_value < 35:
            return "BMI 過高，中度肥胖"
        else:
            return "BMI 過高，重度肥胖"
# 設定 按鈕
bmi_button = tk.Button(window, text="BMI 測量", foreground="blue", font=("標楷體", 12), padx=30, pady=20, command=BMI)
bmi_button.pack()
window.mainloop()