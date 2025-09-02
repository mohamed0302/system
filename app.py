import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import pandas as pd
import os
import smtplib
import requests
from email.message import EmailMessage
import tkinter.filedialog as fd
import time
import locale

# إعداد دعم اللغة العربية
try:
    locale.setlocale(locale.LC_ALL, 'ar_EG.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_ALL, 'Arabic')
    except:
        pass

def create_arabic_text_widget(parent, **kwargs):
    """create an export variable of py file's (don't make function for if statment in this condition 
    .then use >>T,k to make handle bugs threades 
    )
    إنشاء عنصر نص مع دعم اللغة العربية
    """
    # محاولة استخدام خطوط تدعم اللغة العربية
    arabic_fonts = ["SegoeUI", "Tahoma", "ArialUnicodeMS", "MicrosoftSansSerif", "Arial"]
    default_font = None
    
    for font in arabic_fonts:
        try:
            # اختبار الخط
            test_label = tk.Label(parent, text="اختبار", font=(font, 12))
            test_label.destroy()
            default_font = (font, 12)
            break
        except:
            continue
    
    if default_font is None:
        default_font = ("Arial", 12)
    
    if 'font' not in kwargs:
        kwargs['font'] = default_font
    
    text_widget = tk.Text(parent, **kwargs)
    
    # إضافة دعم الاتجاه من اليمين لليسار
    try:
        text_widget.configure(direction="rtl")
    except:
        pass
    
    # إضافة إعدادات إضافية لدعم اللغة العربية
    try:
        text_widget.configure(insertwidth=2)
        text_widget.configure(selectbackground="#0078d4")
        text_widget.configure(selectforeground="white")
    except:
        pass
    
    return text_widget

def create_arabic_entry_widget(parent, **kwargs):
    """
    إنشاء عنصر إدخال مع دعم اللغة العربية
    """
    # محاولة استخدام خطوط تدعم اللغة العربية
    arabic_fonts = ["SegoeUI", "Tahoma", "ArialUnicodeMS", "MicrosoftSansSerif", "Arial"]
    default_font = None
    
    for font in arabic_fonts:
        try:
            # اختبار الخط
            test_label = tk.Label(parent, text="اختبار", font=(font, 12))
            test_label.destroy()
            default_font = (font, 12)
            break
        except:
            continue
    
    if default_font is None:
        default_font = ("Arial", 12)
    
    if 'font' not in kwargs:
        kwargs['font'] = default_font
    
    entry_widget = tk.Entry(parent, **kwargs)
    
    # إضافة إعدادات إضافية لدعم اللغة العربية
    try:
        entry_widget.configure(insertwidth=2)
        entry_widget.configure(selectbackground="#0078d4")
        entry_widget.configure(selectforeground="white")
    except:
        pass
    
    return entry_widget

def add_copy_paste_support(widget):
    """
    إضافة دعم النسخ واللصق والقص لعنصر النص
    """
    def copy_text(event=None):
        try:
            widget.event_generate("<<Copy>>")
        except:
            pass
    
    def paste_text(event=None):
        try:
            widget.event_generate("<<Paste>>")
        except:
            pass
    
    def cut_text(event=None):
        try:
            widget.event_generate("<<Cut>>")
        except:
            pass
    
    def select_all(event=None):
        try:
            widget.select_range(0, tk.END)
            widget.icursor(tk.END)
        except:
            pass
    
    # ربط المفاتيح بالوظائف
    widget.bind("<Control-c>", copy_text)
    widget.bind("<Control-v>", paste_text)
    widget.bind("<Control-x>", cut_text)
    widget.bind("<Control-a>", select_all)
    
    # إضافة قائمة منبثقة للنسخ واللصق
    def show_context_menu(event):
        try:
            context_menu = tk.Menu(widget, tearoff=0)
            context_menu.add_command(label="نسخ", command=copy_text)
            context_menu.add_command(label="لصق", command=paste_text)
            context_menu.add_command(label="قص", command=cut_text)
            context_menu.add_separator()
            context_menu.add_command(label="تحديد الكل", command=select_all)
            context_menu.tk_popup(event.x_root, event.y_root)
        except:
            pass
    
    widget.bind("<Button-3>", show_context_menu)  # النقر بالزر الأيمن

EMAIL_ADDRESS = "mohamed0kassem1@gmail.com"  # ✉️ ضع بريدك
EMAIL_PASSWORD = "ycnl apag djcf kebs"    # 🔐 ضع كلمة مرور التطبيقات
WAPILOT_API_KEY = "dmQI5VXVM6pQnkiv3S2WY8tKWxM4bU7CvLV05eynJP"    # 🔑 ضع API key بتاعك من Wapilot (احصل عليه من https://wapilot.net)
WAPILOT_INSTANCE_ID = "instance1649"    # 🔑 ضع Instance ID بتاعك من Wapilot

def send_email(to_address, subject, body, attachments=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_address
    msg.set_content(body)

    # إضافة المرفقات إذا وجدت
    if attachments:
        for attachment_path in attachments:
            if os.path.exists(attachment_path):
                try:
                    with open(attachment_path, 'rb') as f:
                        file_data = f.read()
                        file_name = os.path.basename(attachment_path)
                        
                        # تحديد نوع الملف
                        if attachment_path.lower().endswith('.pdf'):
                            maintype, subtype = 'application', 'pdf'
                        elif attachment_path.lower().endswith(('.jpg', '.jpeg')):
                            maintype, subtype = 'image', 'jpeg'
                        elif attachment_path.lower().endswith('.png'):
                            maintype, subtype = 'image', 'png'
                        elif attachment_path.lower().endswith('.gif'):
                            maintype, subtype = 'image', 'gif'
                        else:
                            maintype, subtype = 'application', 'octet-stream'
                        
                        msg.add_attachment(file_data, maintype=maintype, subtype=subtype, filename=file_name)
                except Exception as e:
                    print(f"خطأ في إضافة المرفق {attachment_path}: {e}")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def format_phone_number(phone):
    try:
        # تحويل الرقم إلى نص وإزالة المسافات والرموز
        phone = str(phone).strip().replace(' ', '').replace('-', '').replace('.', '')
        
        # إذا الرقم بيبدأ بـ +2 (دولي) - نزيل الـ + ونرجع الرقم بدون +
        if phone.startswith('+2'):
            return phone[1:]  # نزيل الـ + ونرجع الرقم بدون +
        # إذا الرقم بيبدأ بـ 0 (محلي) - نزيل الـ 0 ونضيف 2
        elif phone.startswith('0'):
            return '2' + phone[1:]
        # إذا الرقم بيبدأ بـ 2 (دولي بدون +) - نرجع الرقم كما هو
        elif phone.startswith('2'):
            return phone
        # لو الرقم مش بيبدأ بأي من دول، نضيف 2 في الأول
        else:
            return '2' + phone
    except Exception as e:
        raise ValueError(f"خطأ في تنسيق رقم الهاتف: {str(e)}")

def send_image_via_whatsapp(phone_number, file_path, caption=""):
    """إرسال صورة عبر WhatsApp API"""
    try:
        import requests
        
        # إعدادات API
        API_URL = "https://wapilot.net/api/v1/{instance_id}/send-image"
        API_TOKEN = WAPILOT_API_KEY
        INSTANCE_ID = WAPILOT_INSTANCE_ID
        
        # تحديث URL
        api_url = API_URL.format(instance_id=INSTANCE_ID)
        
        # إعداد البيانات
        data = {
            'token': API_TOKEN,
            'chat_id': phone_number,
            'caption': caption
        }
        
        # إرسال الصورة
        with open(file_path, 'rb') as file:
            file_name = os.path.basename(file_path)
            
            # تحديد نوع MIME للصورة
            file_extension = os.path.splitext(file_path)[1].lower()
            mime_type = 'image/jpeg'  # افتراضي
            
            if file_extension in ['.jpg', '.jpeg']:
                mime_type = 'image/jpeg'
            elif file_extension in ['.png']:
                mime_type = 'image/png'
            elif file_extension in ['.gif']:
                mime_type = 'image/gif'
            elif file_extension in ['.bmp']:
                mime_type = 'image/bmp'
            elif file_extension in ['.tiff', '.tif']:
                mime_type = 'image/tiff'
            elif file_extension in ['.webp']:
                mime_type = 'image/webp'
            elif file_extension in ['.svg']:
                mime_type = 'image/svg+xml'
            
            # طباعة معلومات التشخيص
            print(f"إرسال صورة: {file_path}")
            print(f"إلى رقم: {phone_number}")
            print(f"نوع MIME: {mime_type}")
            print(f"حجم الملف: {os.path.getsize(file_path)} بايت")
            
            # إرسال الصورة مع البيانات الصحيحة
            files = {
                'media': (file_name, file, mime_type)
            }
            
            # إرسال الطلب مع headers مناسبة
            headers = {
                'User-Agent': 'StudentNotifierApp/1.0'
            }
            
            response = requests.post(api_url, data=data, files=files, headers=headers, timeout=30)
            
        # طباعة معلومات التشخيص
        print(f"استجابة API: {response.status_code}")
        print(f"محتوى الاستجابة: {response.text}")
        
        if response.status_code == 200:
            return True, "تم إرسال الصورة بنجاح"
        else:
            return False, f"فشل إرسال الصورة: {response.status_code} - {response.text}"
            
    except Exception as e:
        print(f"خطأ في إرسال الصورة: {str(e)}")
        print(f"نوع الخطأ: {type(e).__name__}")
        import traceback
        print(f"تفاصيل الخطأ: {traceback.format_exc()}")
        return False, f"خطأ في إرسال الصورة: {str(e)}"

def send_file_via_whatsapp(phone_number, file_path, caption=""):
    """إرسال ملف عبر WhatsApp API"""
    try:
        import requests
        
        # تحديد نوع الملف بناءً على امتداده
        file_extension = os.path.splitext(file_path)[1].lower()
        
        # إذا كان الملف صورة، استخدم send-image endpoint
        image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg']
        if file_extension in image_extensions:
            return send_image_via_whatsapp(phone_number, file_path, caption)
        
        # إعدادات API للملفات الأخرى
        API_URL = "https://wapilot.net/api/v1/{instance_id}/send-file"
        API_TOKEN = WAPILOT_API_KEY
        INSTANCE_ID = WAPILOT_INSTANCE_ID
        
        # تحديث URL
        api_url = API_URL.format(instance_id=INSTANCE_ID)
        
        # إعداد البيانات
        data = {
            'token': API_TOKEN,
            'chat_id': phone_number,
            'caption': caption
        }
        
        # إرسال الملف - إصلاح المشكلة
        with open(file_path, 'rb') as file:
            # تحديد اسم الملف مع امتداده
            file_name = os.path.basename(file_path)
            
            # تحديد نوع MIME بناءً على امتداد الملف
            mime_type = 'application/octet-stream'  # افتراضي
            
            # دعم أنواع الملفات المختلفة
            if file_extension in ['.pdf']:
                mime_type = 'application/pdf'
            elif file_extension in ['.doc', '.docx']:
                mime_type = 'application/msword'
            elif file_extension in ['.xls', '.xlsx']:
                mime_type = 'application/vnd.ms-excel'
            elif file_extension in ['.zip', '.rar', '.7z']:
                mime_type = 'application/zip'
            elif file_extension in ['.txt']:
                mime_type = 'text/plain'
            
            # طباعة معلومات التشخيص بعد تعريف mime_type
            print(f"إرسال ملف: {file_path}")
            print(f"إلى رقم: {phone_number}")
            print(f"نوع MIME: {mime_type}")
            print(f"حجم الملف: {os.path.getsize(file_path)} بايت")
            
            # إرسال الملف مع البيانات الصحيحة
            files = {
                'media': (file_name, file, mime_type)
            }
            
            # إرسال الطلب مع headers مناسبة
            headers = {
                'User-Agent': 'StudentNotifierApp/1.0'
            }
            
            response = requests.post(api_url, data=data, files=files, headers=headers, timeout=30)
            
        # طباعة معلومات التشخيص
        print(f"استجابة API: {response.status_code}")
        print(f"محتوى الاستجابة: {response.text}")
        
        if response.status_code == 200:
            return True, "تم إرسال الملف بنجاح"
        else:
            return False, f"فشل إرسال الملف: {response.status_code} - {response.text}"
            
    except Exception as e:
        print(f"خطأ في إرسال الملف: {str(e)}")
        print(f"نوع الخطأ: {type(e).__name__}")
        import traceback
        print(f"تفاصيل الخطأ: {traceback.format_exc()}")
        return False, f"خطأ في إرسال الملف: {str(e)}"

def send_whatsapp(to_number, message):
    try:
        # تنسيق رقم الهاتف
        phone = format_phone_number(to_number)
        
        # استخدام API الخاص بـ Wapilot مع Instance ID
        url = f"https://wapilot.net/api/v1/{WAPILOT_INSTANCE_ID}/send-message"
        headers = {
            "Content-Type": "application/json"
        }
        # تنسيق البيانات حسب متطلبات Wapilot API الجديدة
        data = {
            "token": WAPILOT_API_KEY,
            "chat_id": phone,
            "text": message
        }
        print(f"جاري الإرسال إلى {phone}...")
        print(f"URL المستخدم: {url}")
        print(f"بيانات الإرسال: {data}")
        
        response = requests.post(url, headers=headers, json=data, timeout=30)
        print(f"الرد من الخادم: {response.status_code}")
        print(f"محتوى الرد: {response.text}")
        
        if response.status_code == 401:
            raise Exception("خطأ في API key أو Instance ID. يرجى التحقق من صحة المفاتيح.")
        elif response.status_code == 400:
            error_data = response.json()
            error_message = error_data.get('message', 'خطأ في البيانات المرسلة')
            if 'error' in error_data:
                error_message += f": {error_data['error']}"
            raise Exception(f"خطأ في البيانات المرسلة: {error_message}")
        elif response.status_code == 422:
            error_data = response.json()
            error_message = error_data.get('message', 'خطأ في البيانات المرسلة')
            if 'errors' in error_data:
                errors = error_data['errors']
                error_details = []
                for field, messages in errors.items():
                    error_details.extend(messages)
                error_message = "\n".join(error_details)
            raise Exception(f"خطأ في البيانات المرسلة: {error_message}")
        elif response.status_code == 429:
            # خطأ 429 يعني أننا تجاوزنا الحد المسموح به من الرسائل
            raise Exception("خطأ 429: تم تجاوز الحد المسموح به من الرسائل. الخدمة تطلب منا الإبطاء.")
        elif response.status_code == 500:
            # خطأ 500 - خطأ في الخادم، نعيد المحاولة بعد انتظار قصير
            raise Exception("خطأ 500: خطأ في الخادم. سيتم إعادة المحاولة تلقائياً.")
        elif response.status_code != 200:
            raise Exception(f"خطأ في الخادم: {response.status_code}")
            
        response.raise_for_status()
        return True
    except ValueError as e:
        print(f"خطأ في تنسيق الرقم: {str(e)}")
        raise Exception(str(e))
    except requests.exceptions.ConnectionError as e:
        print(f"تفاصيل خطأ الاتصال: {str(e)}")
        raise Exception("فشل الاتصال بخدمة الواتساب. يرجى التحقق من اتصال الإنترنت.")
    except requests.exceptions.Timeout:
        raise Exception("انتهت مهلة الاتصال بخدمة الواتساب. يرجى المحاولة مرة أخرى.")
    except requests.exceptions.RequestException as e:
        print(f"تفاصيل الخطأ: {str(e)}")
        raise Exception(f"حدث خطأ أثناء الاتصال بخدمة الواتساب: {str(e)}")
    except Exception as e:
        print(f"خطأ غير متوقع: {str(e)}")
        return False

def send_whatsapp_batch(records, message_func, batch_size=60, delay_minutes=1, attachments=None):
    """
    إرسال رسائل الواتساب على دفعات لتجنب خطأ 429
    مع إعادة المحاولة تلقائياً إذا حدث خطأ 429 (Too Many Requests)
    Args:
        records: قائمة السجلات المراد الإرسال إليها
        message_func: دالة تأخذ record وترجع نص الرسالة
        batch_size: عدد الرسائل في كل دفعة (افتراضي 60)
        delay_minutes: التأخير بالدقائق بين الدفعات (افتراضي 1)
        attachments: قائمة مسارات الملفات المرفقة (اختياري)
    Returns:
        tuple: (عدد الرسائل المرسلة بنجاح, عدد الرسائل الفاشلة, قائمة رسائل الأخطاء)
    """
    import time
    total_records = len(records)
    total_batches = (total_records + batch_size - 1) // batch_size
    estimated_time = (total_batches - 1) * delay_minutes  # لا ننتظر بعد آخر دفعة
    print(f"📤 سيتم إرسال {total_records} رسالة على {total_batches} دفعة.")
    print(f"⏱️ الوقت المتوقع: حوالي {estimated_time} دقيقة.")
    success_count = 0
    failed_count = 0
    failed_msgs = []
    
    # التحقق من وجود أرقام متكررة
    phone_numbers = [record["الهاتف"] for record in records if record["الهاتف"] and str(record["الهاتف"]).strip() != "nan"]
    unique_phones = set(phone_numbers)
    if len(phone_numbers) != len(unique_phones):
        print(f"⚠️ تحذير: تم اكتشاف {len(phone_numbers) - len(unique_phones)} رقم مكرر.")
        print("⏰ سيتم زيادة مدة الانتظار بين الرسائل لتجنب منع الرسائل.")
        delay_minutes = max(delay_minutes, 2)  # زيادة مدة الانتظار على الأقل إلى دقيقتين
    
    for i in range(0, total_records, batch_size):
        batch = records[i:i + batch_size]
        batch_num = (i // batch_size) + 1
        print(f"📦 جاري إرسال الدفعة {batch_num} من {total_batches} ({len(batch)} رسالة)...")
        for record in batch:
            if record["الهاتف"] and str(record["الهاتف"]).strip() != "nan":
                try:
                    msg = message_func(record)
                    try:
                        # إرسال الرسالة النصية
                        success = send_whatsapp(record["الهاتف"], msg)
                        if not success:
                            raise Exception("فشل إرسال الرسالة")
                        
                        # إرسال المرفقات إذا وجدت
                        if attachments:
                            for file_path in attachments:
                                try:
                                    # التحقق من وجود الملف
                                    if not os.path.exists(file_path):
                                        print(f"⚠️ تحذير: الملف {file_path} غير موجود")
                                        continue
                                    
                                    # إرسال الملف عبر WhatsApp API
                                    print(f"📎 جاري إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']}...")
                                    success, result = send_file_via_whatsapp(
                                        record["الهاتف"], 
                                        file_path, 
                                        f"مرفق: {os.path.basename(file_path)}"
                                    )
                                    if success:
                                        print(f"✅ تم إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']}")
                                    else:
                                        print(f"❌ فشل إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']}: {result}")
                                        # لا نوقف العملية إذا فشل إرسال مرفق واحد
                                    # انتظار قصير بين المرفقات
                                    time.sleep(1)
                                except Exception as e:
                                    print(f"❌ خطأ في إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']}: {str(e)}")
                                    # لا نوقف العملية إذا فشل إرسال مرفق واحد
                        
                        success_count += 1
                        print(f"✅ تم إرسال رسالة إلى {record['الاسم']}")
                        # انتظار قصير بين كل رسالة لتجنب السبام
                        time.sleep(2)
                    except Exception as e:
                        # معالجة خطأ 429: إعادة المحاولة بعد انتظار أطول
                        if "429" in str(e):
                            print("🔄 تم تجاوز الحد المسموح به. الانتظار 5 دقائق ثم إعادة المحاولة...")
                            time.sleep(5 * 60)
                            try:
                                send_whatsapp(record["الهاتف"], msg)
                                
                                # إعادة إرسال المرفقات بعد إعادة المحاولة
                                if attachments:
                                    for file_path in attachments:
                                        try:
                                            if os.path.exists(file_path):
                                                print(f"🔄 إعادة إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']}...")
                                                success, result = send_file_via_whatsapp(
                                                    record["الهاتف"], 
                                                    file_path, 
                                                    f"مرفق: {os.path.basename(file_path)}"
                                                )
                                                if success:
                                                    print(f"✅ تم إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']} بعد إعادة المحاولة")
                                                else:
                                                    print(f"❌ فشل إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']} بعد إعادة المحاولة: {result}")
                                                time.sleep(1)
                                        except Exception as e2:
                                            print(f"❌ خطأ في إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']} بعد إعادة المحاولة: {str(e2)}")
                                
                                success_count += 1
                                print(f"✅ تم إرسال رسالة إلى {record['الاسم']} بعد إعادة المحاولة")
                                time.sleep(2)
                            except Exception as e2:
                                failed_count += 1
                                failed_msgs.append(f"{record['الاسم']}: {str(e2)}")
                                print(f"❌ فشل إرسال رسالة إلى {record['الاسم']} بعد إعادة المحاولة: {str(e2)}")
                        # معالجة خطأ 500: إعادة المحاولة بعد انتظار قصير
                        elif "500" in str(e):
                            print("🔄 خطأ في الخادم. الانتظار 30 ثانية ثم إعادة المحاولة...")
                            time.sleep(30)
                            try:
                                send_whatsapp(record["الهاتف"], msg)
                                
                                # إعادة إرسال المرفقات بعد إعادة المحاولة
                                if attachments:
                                    for file_path in attachments:
                                        try:
                                            if os.path.exists(file_path):
                                                print(f"🔄 إعادة إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']}...")
                                                success, result = send_file_via_whatsapp(
                                                    record["الهاتف"], 
                                                    file_path, 
                                                    f"مرفق: {os.path.basename(file_path)}"
                                                )
                                                if success:
                                                    print(f"✅ تم إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']} بعد إعادة المحاولة")
                                                else:
                                                    print(f"❌ فشل إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']} بعد إعادة المحاولة: {result}")
                                                time.sleep(1)
                                        except Exception as e2:
                                            print(f"❌ خطأ في إرسال المرفق {os.path.basename(file_path)} إلى {record['الاسم']} بعد إعادة المحاولة: {str(e2)}")
                                
                                success_count += 1
                                print(f"✅ تم إرسال رسالة إلى {record['الاسم']} بعد إعادة المحاولة")
                                time.sleep(2)
                            except Exception as e2:
                                failed_count += 1
                                failed_msgs.append(f"{record['الاسم']}: {str(e2)}")
                                print(f"❌ فشل إرسال رسالة إلى {record['الاسم']}: {str(e2)}")
                        else:
                            failed_count += 1
                            failed_msgs.append(f"{record['الاسم']}: {str(e)}")
                            print(f"❌ فشل إرسال رسالة إلى {record['الاسم']}: {str(e)}")
                except Exception as e:
                    failed_count += 1
                    failed_msgs.append(f"{record['الاسم']}: {str(e)}")
                    print(f"❌ فشل إرسال رسالة إلى {record['الاسم']}: {str(e)}")
        # إذا لم تكن آخر دفعة، انتظر قبل الدفعة التالية
        if i + batch_size < total_records:
            print(f"⏳ انتهاء الدفعة {batch_num}. انتظار {delay_minutes} دقيقة قبل الدفعة التالية...")
            time.sleep(delay_minutes * 60)
    return success_count, failed_count, failed_msgs

STUDENT_FILE = "students.csv"
GROUP_FILE = "groups.csv"
LESSON_FILE = "lessons.csv"  # نحتفظ بملف الحصص للقراءة فقط

class StudentNotifierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("برنامج إشعارات أولياء الأمور")
        self.root.geometry("800x600")
        self.root.configure(bg="#2e2e2e")
        
        # إعداد دعم اللغة العربية للنافذة
        try:
            self.root.option_add('*Font', 'SegoeUI 12')
            self.root.option_add('*Text.Font', 'SegoeUI 12')
            self.root.option_add('*Entry.Font', 'SegoeUI 12')
            self.root.option_add('*Label.Font', 'SegoeUI 12')
            self.root.option_add('*Button.Font', 'SegoeUI 12')
        except:
            pass

        # قراءة ملف الحصص (للقراءة والكتابة)
        self.lessons_file = LESSON_FILE
        if os.path.exists(self.lessons_file):
            try:
                self.lessons = pd.read_csv(self.lessons_file, encoding='utf-8-sig', sep=';')
            except UnicodeDecodeError:
                self.lessons = pd.read_csv(self.lessons_file, encoding='cp1256', sep=';')
        else:
            # إنشاء ملف الحصص الافتراضي إذا لم يكن موجوداً
            self.lessons = pd.DataFrame(columns=["الحصة", "الوقت", "الوصف"])
            self.save_lessons()

        # إضافة ملف الواجبات
        # self.homework_file = "homework.csv"
        # if os.path.exists(self.homework_file):
        #     try:
        #         self.homework = pd.read_csv(self.homework_file, encoding='utf-8-sig', sep=';')
        #     except UnicodeDecodeError:
        #         self.homework = pd.read_csv(self.homework_file, encoding='cp1256', sep=';')
        # else:
        #     self.homework = pd.DataFrame(columns=["المجموعة", "التاريخ", "الواجب", "الحالة", "ملاحظات"])

        # إضافة ملف حالة الواجبات
        # self.homework_status_file = "homework_status.csv"
        # if os.path.exists(self.homework_status_file):
        #     try:
        #         self.homework_status = pd.read_csv(self.homework_status_file, encoding='utf-8-sig', sep=';')
        #     except UnicodeDecodeError:
        #         self.homework_status = pd.read_csv(self.homework_status_file, encoding='cp1256', sep=';')
        # else:
        #     self.homework_status = pd.DataFrame(columns=["الاسم", "المجموعة", "التاريخ", "الواجب", "الحالة", "ملاحظات"])

        # قراءة ملف الطلاب مع دعم اللغة العربية
        if os.path.exists(STUDENT_FILE):
            try:
                self.students = pd.read_csv(STUDENT_FILE, encoding='utf-8-sig', sep=';', dtype={"الهاتف": str})
                if "الهاتف" not in self.students.columns:
                    self.students["الهاتف"] = ""
                    self.students.to_csv(STUDENT_FILE, index=False, encoding='utf-8-sig', sep=';')
            except UnicodeDecodeError:
                # إذا فشل الترميز الأول، نحاول ترميز آخر
                self.students = pd.read_csv(STUDENT_FILE, encoding='cp1256', sep=';', dtype={"الهاتف": str})
                if "الهاتف" not in self.students.columns:
                    self.students["الهاتف"] = ""
                    self.students.to_csv(STUDENT_FILE, index=False, encoding='utf-8-sig', sep=';')
        else:
            self.students = pd.DataFrame(columns=["الاسم", "الصف", "البريد", "المجموعة", "الهاتف"])

        # قراءة ملف المجموعات مع دعم اللغة العربية
        if os.path.exists(GROUP_FILE):
            try:
                self.groups = pd.read_csv(GROUP_FILE, encoding='utf-8-sig', sep=';')
                if "الصف" not in self.groups.columns:
                    self.groups["الصف"] = "غير محدد"
                    self.groups.to_csv(GROUP_FILE, index=False, encoding='utf-8-sig', sep=';')
            except UnicodeDecodeError:
                # إذا فشل الترميز الأول، نحاول ترميز آخر
                self.groups = pd.read_csv(GROUP_FILE, encoding='cp1256', sep=';')
                if "الصف" not in self.groups.columns:
                    self.groups["الصف"] = "غير محدد"
                    self.groups.to_csv(GROUP_FILE, index=False, encoding='utf-8-sig', sep=';')
        else:
            self.groups = pd.DataFrame(columns=["المجموعة", "الصف"])

        self.name_label = tk.Label(root, text="اسم الطالب:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12))
        self.name_label.pack()
        self.name_entry = create_arabic_entry_widget(root)
        add_copy_paste_support(self.name_entry)
        self.name_entry.pack()

        self.grade_label = tk.Label(root, text="الصف:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12))
        self.grade_label.pack()
        self.grade_combo = ttk.Combobox(root, values=["الصف الأول الثانوي", "الصف الثاني الثانوي", "الصف الثالث الثانوي"], font=("SegoeUI", 12), state="readonly")
        self.grade_combo.pack()
        # إضافة تتبع لتغيير الصف
        self.grade_combo.bind('<<ComboboxSelected>>', self.update_group_combo_by_grade)

        self.email_label = tk.Label(root, text="بريد ولي الأمر:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12))
        self.email_entry = create_arabic_entry_widget(root)
        add_copy_paste_support(self.email_entry)
        self.email_label.pack()
        self.email_entry.pack()

        self.phone_label = tk.Label(root, text="رقم هاتف ولي الأمر:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12))
        self.phone_entry = create_arabic_entry_widget(root)
        add_copy_paste_support(self.phone_entry)
        self.phone_label.pack()
        self.phone_entry.pack()

        self.group_label = tk.Label(root, text="اختر المجموعة:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12))
        self.group_label.pack()
        self.group_combo = ttk.Combobox(root, values=self.groups["المجموعة"].tolist() if not self.groups.empty else [], state="readonly", font=("SegoeUI", 12))
        self.group_combo.pack()

        self.add_button = tk.Button(root, text="إضافة الطالب", command=self.add_student, bg="#00cc66", fg="white", font=("SegoeUI", 12))
        self.add_button.pack(pady=10)

        self.manage_groups_btn = tk.Button(root, text="إدارة المجموعات", command=self.manage_groups, bg="#ff6600", fg="white", font=("SegoeUI", 12))
        self.manage_groups_btn.pack(pady=5)
        
        # إضافة إعدادات إضافية لدعم اللغة العربية
        try:
            # إعداد النافذة لدعم اللغة العربية
            self.root.update_idletasks()
            
            # إضافة دعم للنسخ واللصق باللغة العربية
            def arabic_paste(event=None):
                try:
                    import pyperclip
                    text = pyperclip.paste()
                    if hasattr(event.widget, 'insert'):
                        event.widget.insert(tk.INSERT, text)
                    return 'break'
                except:
                    pass
            
            # ربط دالة اللصق باللغة العربية
            self.root.bind('<Control-v>', arabic_paste)
        except:
            pass

        self.view_groups_btn = tk.Button(root, text="عرض المجموعات", command=self.view_groups_with_checkboxes, bg="#3399ff", fg="white", font=("SegoeUI", 12))
        self.view_groups_btn.pack(pady=5)

        # إضافة زر إدارة الحصص
        self.manage_lessons_btn = tk.Button(root, text="إدارة الحصص", command=self.manage_lessons, bg="#9933ff", fg="white", font=("SegoeUI", 12))
        self.manage_lessons_btn.pack(pady=5)

        # إضافة زر إدارة الامتحانات والدرجات
        self.manage_exams_btn = tk.Button(root, text="إدارة الامتحانات والدرجات", command=self.manage_exams, bg="#ff6600", fg="white", font=("SegoeUI", 12))
        self.manage_exams_btn.pack(pady=5)

        # زر استيراد الطلاب من CSV
        import_csv_btn = tk.Button(root, text="استيراد طلاب من CSV", command=self.import_students_from_csv, bg="#cccccc", fg="black", font=("SegoeUI", 12))
        import_csv_btn.pack(pady=5)

        # زر استيراد المجموعات من CSV
        import_groups_btn = tk.Button(root, text="استيراد مجموعات من CSV", command=self.import_groups_from_csv, bg="#cccccc", fg="black", font=("SegoeUI", 12))
        import_groups_btn.pack(pady=5)

    def update_group_combo_by_grade(self, event=None):
        """تحديث قائمة المجموعات بناءً على الصف المختار"""
        selected_grade = self.grade_combo.get()
        if selected_grade:
            # تصفية المجموعات حسب الصف المختار
            filtered_groups = self.groups[self.groups["الصف"] == selected_grade]["المجموعة"].tolist()
            self.group_combo['values'] = filtered_groups
            # مسح الاختيار الحالي
            self.group_combo.set('')
        else:
            # إذا لم يتم اختيار صف، عرض جميع المجموعات
            self.group_combo['values'] = self.groups["المجموعة"].tolist()
            self.group_combo.set('')

    def add_student(self):
        name = self.name_entry.get().strip()
        grade = self.grade_combo.get().strip()
        email = self.email_entry.get().strip()
        group = self.group_combo.get().strip()
        phone = self.phone_entry.get().strip()

        if not (name and grade and (email or phone)):
            messagebox.showwarning("تنبيه", "يرجى ملء الاسم والصف ورقم الهاتف أو البريد الإلكتروني على الأقل.")
            return

        new_row = {"الاسم": name, "الصف": grade, "البريد": email, "المجموعة": group, "الهاتف": phone}
        self.students = pd.concat([self.students, pd.DataFrame([new_row])], ignore_index=True)
        self.students.to_csv(STUDENT_FILE, index=False, encoding='utf-8-sig', sep=';')
        messagebox.showinfo("تم", "تمت إضافة الطالب.")
        self.name_entry.delete(0, tk.END)
        self.grade_combo.set('')
        self.email_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.group_combo.set('')

    def manage_groups(self):
        win = tk.Toplevel(self.root)
        win.title("إدارة المجموعات")
        win.geometry("400x600")
        win.configure(bg="#2e2e2e")

        # إطار البحث
        search_frame = tk.Frame(win, bg="#2e2e2e")
        search_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(search_frame, text="بحث:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
        search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=search_var, font=("SegoeUI", 12), width=20)
        search_entry.pack(side="left", padx=5)

        # إطار تصفية الصف
        filter_frame = tk.Frame(win, bg="#2e2e2e")
        filter_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(filter_frame, text="تصفية حسب الصف:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
        grade_filter_var = tk.StringVar(value="الكل")
        grade_filter_combo = ttk.Combobox(filter_frame, textvariable=grade_filter_var, 
                                        values=["الكل", "الصف الأول الثانوي", "الصف الثاني الثانوي", "الصف الثالث الثانوي", "غير محدد"],
                                        state="readonly", font=("SegoeUI", 12), width=15)
        grade_filter_combo.pack(side="left", padx=5)

        # إنشاء إطار للقائمة
        list_frame = tk.Frame(win, bg="#2e2e2e")
        list_frame.pack(fill="both", expand=True, pady=10, padx=10)

        # إضافة عناوين الأعمدة
        headers_frame = tk.Frame(list_frame, bg="#2e2e2e")
        headers_frame.pack(fill="x")
        
        tk.Label(headers_frame, text="المجموعة", width=20, bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
        tk.Label(headers_frame, text="الصف", width=20, bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)

        # إنشاء قائمة المجموعات مع الصفوف
        group_listbox = tk.Listbox(list_frame, font=("SegoeUI", 12), height=10)
        group_listbox.pack(fill="both", expand=True)

        def update_group_list(*args):
            # مسح القائمة الحالية
            group_listbox.delete(0, tk.END)
            
            # الحصول على قيم البحث والتصفية
            search_text = search_var.get().strip().lower()
            grade_filter = grade_filter_var.get()
            
            for _, row in self.groups.iterrows():
                group_name = row["المجموعة"]
                group_grade = row.get("الصف", "غير محدد")
                
                # التحقق من تطابق معايير البحث والتصفية
                matches_search = False
                # 1. البحث في اسم المجموعة أو الصف
                if not search_text or search_text in group_name.lower() or search_text in group_grade.lower():
                    matches_search = True
                else:
                    # 2. البحث في الطلاب داخل المجموعة
                    group_students = self.students[self.students["المجموعة"] == group_name]
                    for _, student in group_students.iterrows():
                        if (search_text in str(student["الاسم"]).lower() or
                            search_text in str(student["البريد"]).lower() or
                            search_text in str(student.get("الهاتف", "")).lower()):
                            matches_search = True
                            break
                matches_grade = grade_filter == "الكل" or group_grade == grade_filter
                
                if matches_search and matches_grade:
                    group_listbox.insert(tk.END, f"{group_name} - {group_grade}")

        # ربط وظيفة التحديث بتغييرات البحث والتصفية
        search_var.trace("w", update_group_list)
        grade_filter_var.trace("w", update_group_list)

        # عرض المجموعات الأولية
        update_group_list()

        def add_group():
            add_win = tk.Toplevel(win)
            add_win.title("إضافة مجموعة جديدة")
            add_win.geometry("300x200")
            add_win.configure(bg="#2e2e2e")

            tk.Label(add_win, text="اسم المجموعة:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(pady=5)
            name_entry = tk.Entry(add_win, font=("SegoeUI", 12))
            add_copy_paste_support(name_entry)
            name_entry.pack(pady=5)

            tk.Label(add_win, text="اختر الصف:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(pady=5)
            grade_combo = ttk.Combobox(add_win, values=["الصف الأول الثانوي", "الصف الثاني الثانوي", "الصف الثالث الثانوي"], 
                                     state="readonly", font=("SegoeUI", 12))
            grade_combo.pack(pady=5)

            def save_group():
                new_name = name_entry.get().strip()
                new_grade = grade_combo.get().strip()

                if not (new_name and new_grade):
                    messagebox.showwarning("تنبيه", "يرجى ملء جميع الحقول.", parent=add_win)
                    return

                if new_name in self.groups["المجموعة"].values:
                    messagebox.showwarning("تنبيه", "اسم المجموعة موجود بالفعل.", parent=add_win)
                    return

                new_row = pd.DataFrame({"المجموعة": [new_name], "الصف": [new_grade]})
                self.groups = pd.concat([self.groups, new_row], ignore_index=True)
                self.groups.to_csv(GROUP_FILE, index=False, encoding='utf-8-sig', sep=';')
                
                group_listbox.insert(tk.END, f"{new_name} - {new_grade}")
                self.group_combo['values'] = self.groups["المجموعة"].tolist()
                add_win.destroy()
                messagebox.showinfo("تم", "تمت إضافة المجموعة بنجاح.", parent=win)

            tk.Button(add_win, text="حفظ", command=save_group, bg="#00cc66", fg="white", 
                     font=("SegoeUI", 12)).pack(pady=10)

        def delete_group():
            selected = group_listbox.curselection()
            if not selected:
                messagebox.showwarning("تنبيه", "اختر مجموعة للحذف.", parent=win)
                return
            
            idx = selected[0]
            group_info = group_listbox.get(idx)
            group_name = group_info.split(" - ")[0]
            
            confirm = messagebox.askyesno("تأكيد", f"هل تريد حذف المجموعة '{group_name}'؟", parent=win)
            if confirm:
                self.groups = self.groups[self.groups["المجموعة"] != group_name]
                self.groups.to_csv(GROUP_FILE, index=False, encoding='utf-8-sig', sep=';')
                group_listbox.delete(idx)
                self.group_combo['values'] = self.groups["المجموعة"].tolist()

        def rename_group():
            selected = group_listbox.curselection()
            if not selected:
                messagebox.showwarning("تنبيه", "اختر مجموعة لتعديلها.", parent=win)
                return

            idx = selected[0]
            group_info = group_listbox.get(idx)
            old_name = group_info.split(" - ")[0]
            old_grade = group_info.split(" - ")[1]

            edit_win = tk.Toplevel(win)
            edit_win.title("تعديل المجموعة")
            edit_win.geometry("300x200")
            edit_win.configure(bg="#2e2e2e")

            tk.Label(edit_win, text="اسم المجموعة:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(pady=5)
            name_entry = tk.Entry(edit_win, font=("SegoeUI", 12))
            add_copy_paste_support(name_entry)
            name_entry.insert(0, old_name)
            name_entry.pack(pady=5)

            tk.Label(edit_win, text="اختر الصف:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(pady=5)
            grade_combo = ttk.Combobox(edit_win, values=["الصف الأول الثانوي", "الصف الثاني الثانوي", "الصف الثالث الثانوي"], 
                                     state="readonly", font=("SegoeUI", 12))
            grade_combo.set(old_grade)
            grade_combo.pack(pady=5)

            def save_changes():
                new_name = name_entry.get().strip()
                new_grade = grade_combo.get().strip()

                if not (new_name and new_grade):
                    messagebox.showwarning("تنبيه", "يرجى ملء جميع الحقول.", parent=edit_win)
                    return

                if new_name != old_name and new_name in self.groups["المجموعة"].values:
                    messagebox.showwarning("تنبيه", "اسم المجموعة موجود بالفعل.", parent=edit_win)
                    return

                # تحديث اسم المجموعة في جدول الطلاب
                self.students.loc[self.students["المجموعة"] == old_name, "المجموعة"] = new_name
                self.students.to_csv(STUDENT_FILE, index=False, encoding='utf-8-sig', sep=';')

                # تحديث بيانات المجموعة
                self.groups.loc[self.groups["المجموعة"] == old_name, ["المجموعة", "الصف"]] = [new_name, new_grade]
                self.groups.to_csv(GROUP_FILE, index=False, encoding='utf-8-sig', sep=';')

                group_listbox.delete(idx)
                group_listbox.insert(idx, f"{new_name} - {new_grade}")
                self.group_combo['values'] = self.groups["المجموعة"].tolist()
                
                edit_win.destroy()
                messagebox.showinfo("تم", "تم تعديل المجموعة بنجاح.", parent=win)

            tk.Button(edit_win, text="حفظ التغييرات", command=save_changes, bg="#00cc66", fg="white", 
                     font=("SegoeUI", 12)).pack(pady=10)

        # أزرار التحكم
        btn_frame = tk.Frame(win, bg="#2e2e2e")
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="إضافة مجموعة", command=add_group, bg="#00cc66", fg="white", font=("SegoeUI", 12))
        add_btn.pack(side="left", padx=5)

        edit_btn = tk.Button(btn_frame, text="تعديل المجموعة", command=rename_group, bg="#ffaa00", fg="black", font=("SegoeUI", 12))
        edit_btn.pack(side="left", padx=5)

        del_btn = tk.Button(btn_frame, text="حذف مجموعة", command=delete_group, bg="#cc3333", fg="white", font=("SegoeUI", 12))
        del_btn.pack(side="left", padx=5)

    def view_groups_with_checkboxes(self):
        win = tk.Toplevel(self.root)
        win.title("عرض الطلاب داخل المجموعات")
        win.geometry("1000x600")
        win.configure(bg="#2e2e2e")

        # إطار البحث والتصفية
        filter_frame = tk.Frame(win, bg="#2e2e2e")
        filter_frame.pack(fill="x", padx=10, pady=5)

        # إطار البحث
        search_frame = tk.Frame(filter_frame, bg="#2e2e2e")
        search_frame.pack(side="left", padx=10)
        
        tk.Label(search_frame, text="بحث:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
        search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=search_var, font=("SegoeUI", 12), width=20)
        add_copy_paste_support(search_entry)
        search_entry.pack(side="left", padx=5)

        # إطار تصفية الصف
        grade_frame = tk.Frame(filter_frame, bg="#2e2e2e")
        grade_frame.pack(side="left", padx=10)
        
        tk.Label(grade_frame, text="تصفية حسب الصف:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
        grade_filter_var = tk.StringVar(value="الكل")
        grade_filter_combo = ttk.Combobox(grade_frame, textvariable=grade_filter_var, 
                                        values=["الكل", "الصف الأول الثانوي", "الصف الثاني الثانوي", "الصف الثالث الثانوي", "غير محدد"],
                                        state="readonly", font=("SegoeUI", 12), width=15)
        grade_filter_combo.pack(side="left", padx=5)

        # إطار المحتوى الرئيسي
        content_frame = tk.Frame(win, bg="#2e2e2e")
        content_frame.pack(fill="both", expand=True, padx=10, pady=5)

        # قائمة المجموعات
        groups_frame = tk.Frame(content_frame, bg="#2e2e2e")
        groups_frame.pack(side="left", fill="y", padx=5)

        tk.Label(groups_frame, text="المجموعات", bg="#2e2e2e", fg="white", font=("SegoeUI", 12, "bold")).pack(pady=5)
        group_listbox = tk.Listbox(groups_frame, font=("SegoeUI", 12), height=20, width=30)
        group_listbox.pack(fill="y", expand=True)

        # عرض المجموعات في القائمة
        for _, row in self.groups.iterrows():
            group_name = row["المجموعة"]
            group_grade = row.get("الصف", "غير محدد")
            group_listbox.insert(tk.END, f"{group_name} - {group_grade}")

        def update_group_list(*args):
            # مسح القائمة الحالية
            group_listbox.delete(0, tk.END)
            
            # الحصول على قيم البحث والتصفية
            search_text = search_var.get().strip().lower()
            grade_filter = grade_filter_var.get()
            
            for _, row in self.groups.iterrows():
                group_name = row["المجموعة"]
                group_grade = row.get("الصف", "غير محدد")
                
                # التحقق من تطابق معايير البحث والتصفية
                matches_search = False
                # 1. البحث في اسم المجموعة أو الصف
                if not search_text or search_text in group_name.lower() or search_text in group_grade.lower():
                    matches_search = True
                else:
                    # 2. البحث في الطلاب داخل المجموعة
                    group_students = self.students[self.students["المجموعة"] == group_name]
                    for _, student in group_students.iterrows():
                        if (search_text in str(student["الاسم"]).lower() or
                            search_text in str(student["البريد"]).lower() or
                            search_text in str(student.get("الهاتف", "")).lower()):
                            matches_search = True
                            break
                matches_grade = grade_filter == "الكل" or group_grade == grade_filter
                
                if matches_search and matches_grade:
                    group_listbox.insert(tk.END, f"{group_name} - {group_grade}")

        # جدول الطلاب
        students_frame = tk.Frame(content_frame, bg="#2e2e2e")
        students_frame.pack(side="left", fill="both", expand=True, padx=5)

        # إنشاء الجدول مع عمود التحديد
        tree = ttk.Treeview(students_frame, columns=("select", "name", "grade", "email", "phone", "group"), 
                           show="headings", selectmode="none")
        tree.heading("select", text="تحديد")
        tree.heading("name", text="اسم الطالب")
        tree.heading("grade", text="الصف")
        tree.heading("email", text="البريد")
        tree.heading("phone", text="الهاتف")
        tree.heading("group", text="المجموعة")
        
        # تحديد عرض الأعمدة
        tree.column("select", width=50, anchor="center")
        tree.column("name", width=150)
        tree.column("grade", width=150)
        tree.column("email", width=200)
        tree.column("phone", width=150)
        tree.column("group", width=150)

        # إضافة شريط التمرير للجدول
        scrollbar = ttk.Scrollbar(students_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)
        tree.pack(fill="both", expand=True)

        # تعريف الأيقونات للتحديد
        checked_icon = "☑"
        unchecked_icon = "☐"

        def toggle_check(event):
            item = tree.identify_row(event.y)
            if item:
                current_tags = tree.item(item)['tags']
                current_values = list(tree.item(item)['values'])
                if 'checked' in current_tags:
                    # إلغاء التحديد
                    current_values[0] = unchecked_icon
                    tree.item(item, tags=('unchecked',), values=current_values)
                    tree.selection_remove(item)
                else:
                    # تحديد
                    current_values[0] = checked_icon
                    tree.item(item, tags=('checked',), values=current_values)
                    tree.selection_add(item)

        def select_all():
            for item in tree.get_children():
                current_values = list(tree.item(item)['values'])
                current_values[0] = checked_icon
                tree.item(item, tags=('checked',), values=current_values)
                tree.selection_add(item)

        def deselect_all():
            for item in tree.get_children():
                current_values = list(tree.item(item)['values'])
                current_values[0] = unchecked_icon
                tree.item(item, tags=('unchecked',), values=current_values)
                tree.selection_remove(item)

        # إضافة أزرار التحديد
        buttons_frame = tk.Frame(students_frame, bg="#2e2e2e")
        buttons_frame.pack(fill="x", pady=5)

        select_all_btn = tk.Button(buttons_frame, text="تحديد الكل", command=select_all, 
                                 bg="#00cc66", fg="white", font=("SegoeUI", 12))
        select_all_btn.pack(side="left", padx=5)

        deselect_all_btn = tk.Button(buttons_frame, text="إلغاء التحديد", command=deselect_all, 
                                   bg="#cc3333", fg="white", font=("SegoeUI", 12))
        deselect_all_btn.pack(side="left", padx=5)

        # ربط حدث النقر على الصف
        tree.bind("<Button-1>", toggle_check)

        def show_students(event):
            for item in tree.get_children():
                tree.delete(item)
            selected_students.clear()

            # تطبيق البحث على الطلاب
            search_text = search_var.get().strip().lower()
            grade_filter = grade_filter_var.get()

            # الحصول على المجموعة المختارة
            sel = group_listbox.curselection()
            selected_group = None
            if sel:
                group_info = group_listbox.get(sel[0])
                selected_group = group_info.split(" - ")[0]

            # البحث في الطلاب
            for index, row in self.students.iterrows():
                # التحقق من تطابق معايير البحث والتصفية للطلاب
                matches_search = not search_text or (
                    search_text in str(row["الاسم"]).lower() or 
                    search_text in str(row["الصف"]).lower() or 
                    search_text in str(row["البريد"]).lower() or
                    search_text in str(row.get("الهاتف", "")).lower() or
                    search_text in str(row.get("المجموعة", "")).lower()
                )
                matches_grade = grade_filter == "الكل" or row["الصف"] == grade_filter
                matches_group = not selected_group or str(row.get("المجموعة", "")) == selected_group

                if matches_search and matches_grade and matches_group:
                    iid = str(index)
                    # إضافة الطالب مع أيقونة غير محدد والمجموعة
                    tree.insert("", "end", iid=iid, 
                              values=(unchecked_icon, row["الاسم"], row["الصف"], 
                                    row["البريد"], row.get("الهاتف", ""), row.get("المجموعة", "")), 
                              tags=('unchecked',))

        # ربط وظيفة التحديث بتغييرات البحث والتصفية
        search_var.trace_add('write', lambda *args: (update_group_list(), show_students(None)))
        grade_filter_var.trace_add('write', lambda *args: (update_group_list(), show_students(None)))

        # ربط حدث اختيار المجموعة
        group_listbox.bind("<<ListboxSelect>>", show_students)

        selected_students = []

        def get_selected_students():
            selected = []
            for item in tree.get_children():
                if 'checked' in tree.item(item)['tags']:
                    values = tree.item(item)['values']
                    # نستخدم iid كـ index
                    student_index = int(item)
                    selected.append({
                        "index": student_index,
                        "الاسم": values[1],
                        "الصف": values[2],
                        "البريد": values[3],
                        "الهاتف": values[4] if len(values) > 4 else "",
                        # المجموعة ليست ضرورية للحذف الآن
                    })
            return selected

        def send_reports():
            selected = get_selected_students()
            if not selected:
                messagebox.showwarning("تنبيه", "يرجى تحديد طلاب لإرسال التقارير إليهم.")
                return

            # إنشاء نافذة منبثقة لإدخال نص التقرير
            report_win = tk.Toplevel(win)
            report_win.title("إدخال نص التقرير")
            report_win.geometry("600x400")
            report_win.configure(bg="#2e2e2e")

            # إضافة عنوان
            tk.Label(report_win, text="نص التقرير المراد إرساله:", 
                    bg="#2e2e2e", fg="white", font=("SegoeUI", 12, "bold")).pack(pady=10)



            # إضافة مربع نص متعدد الأسطر
            text_frame = tk.Frame(report_win, bg="#2e2e2e")
            text_frame.pack(fill="both", expand=True, padx=10, pady=5)

            report_text = create_arabic_text_widget(text_frame, height=10, width=50, wrap=tk.WORD)
            add_copy_paste_support(report_text)
            report_text.pack(side="left", fill="both", expand=True)
            
            # إضافة نص افتراضي لاختبار العرض
            report_text.insert("1.0", "أدخل نص التقرير هنا...")
            
            # إضافة إعدادات إضافية لدعم اللغة العربية
            try:
                report_text.configure(insertwidth=2)
                report_text.configure(selectbackground="#0078d4")
                report_text.configure(selectforeground="white")
                report_text.configure(bg="white", fg="black")
            except:
                pass

            # إضافة شريط التمرير
            scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=report_text.yview)
            scrollbar.pack(side="right", fill="y")
            report_text.configure(yscrollcommand=scrollbar.set)

            # إطار للمرفقات
            attachment_frame = tk.Frame(report_win, bg="#2e2e2e")
            attachment_frame.pack(fill="x", padx=10, pady=5)
            
            tk.Label(attachment_frame, text="المرفقات (اختياري):", 
                    bg="#2e2e2e", fg="white", font=("SegoeUI", 11, "bold")).pack(anchor="w", pady=(0, 5))
            
            # تعليمات حول المرفقات
            instructions_text = "💡 ملاحظة: المرفقات تُرسل فعلياً عبر WhatsApp مع دعم كامل للصور والملفات!"
            tk.Label(attachment_frame, text=instructions_text, 
                    bg="#2e2e2e", fg="#00FF00", font=("SegoeUI", 9, "italic")).pack(anchor="w", pady=(0, 5))
            
            # قائمة المرفقات
            attachments_list = []
            
            # إطار لعرض المرفقات المختارة
            attachments_display_frame = tk.Frame(attachment_frame, bg="#2e2e2e")
            attachments_display_frame.pack(fill="x", pady=5)
            
            attachments_listbox = tk.Listbox(attachments_display_frame, height=3, font=("SegoeUI", 10))
            attachments_listbox.pack(side="left", fill="x", expand=True)
            
            # شريط التمرير للمرفقات
            attachments_scrollbar = ttk.Scrollbar(attachments_display_frame, orient="vertical", command=attachments_listbox.yview)
            attachments_scrollbar.pack(side="right", fill="y")
            attachments_listbox.configure(yscrollcommand=attachments_scrollbar.set)
            
            def add_attachment():
                """إضافة مرفق جديد"""
                file_types = [
                    ("ملفات PDF", "*.pdf"),
                    ("صور", "*.jpg *.jpeg *.png *.gif *.bmp *.tiff *.tif *.webp *.svg"),
                    ("ملفات Office", "*.doc *.docx *.xls *.xlsx"),
                    ("ملفات مضغوطة", "*.zip *.rar *.7z"),
                    ("ملفات نصية", "*.txt"),
                    ("جميع الملفات", "*.*")
                ]
                file_path = fd.askopenfilename(
                    title="اختر ملف للإرفاق",
                    filetypes=file_types,
                    parent=report_win
                )
                if file_path:
                    attachments_list.append(file_path)
                    file_name = os.path.basename(file_path)
                    attachments_listbox.insert(tk.END, file_name)
                    
                    # طباعة معلومات الملف المضاف
                    file_extension = os.path.splitext(file_path)[1].lower()
                    if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg']:
                        print(f"✅ تم إضافة صورة: {file_name}")
                        print(f"   النوع: {file_extension.upper()}")
                        print(f"   المسار: {file_path}")
                        
                        # رسالة تأكيد للصور
                        messagebox.showinfo("تم إضافة صورة", 
                            f"تم إضافة الصورة بنجاح:\n\n"
                            f"📸 {file_name}\n"
                            f"🎯 يمكنك الآن استخدام زر 'معاينة' لرؤية الصورة\n"
                            f"🔧 وزر 'تحسين الصورة' لإنشاء نسخة محسنة",
                            parent=report_win)
                    else:
                        print(f"📎 تم إضافة ملف: {file_name}")
                        print(f"   النوع: {file_extension.upper()}")
                        print(f"   المسار: {file_path}")
                        
                        # رسالة تأكيد للملفات الأخرى
                        messagebox.showinfo("تم إضافة ملف", 
                            f"تم إضافة الملف بنجاح:\n\n"
                            f"📎 {file_name}\n"
                            f"🎯 سيتم إرساله مع التقرير",
                            parent=report_win)
            
            def remove_attachment():
                """إزالة المرفق المحدد"""
                selection = attachments_listbox.curselection()
                if not selection:
                    messagebox.showwarning("تنبيه", "يرجى تحديد مرفق للإزالة", parent=report_win)
                    return
                
                index = selection[0]
                
                # فحص أن القائمة ليست فارغة وأن الفهرس صحيح
                if not attachments_list or index >= len(attachments_list):
                    messagebox.showwarning("تنبيه", "لا توجد مرفقات متاحة للإزالة", parent=report_win)
                    return
                
                attachments_list.pop(index)
                attachments_listbox.delete(index)
            
            def clear_attachments():
                """مسح جميع المرفقات"""
                attachments_list.clear()
                attachments_listbox.delete(0, tk.END)
            
            def preview_attachment():
                """معاينة المرفق المحدد (للصور)"""
                selection = attachments_listbox.curselection()
                if not selection:
                    messagebox.showwarning("تنبيه", "يرجى تحديد مرفق للمعاينة", parent=report_win)
                    return
                
                index = selection[0]
                
                # فحص أن القائمة ليست فارغة وأن الفهرس صحيح
                if not attachments_list or index >= len(attachments_list):
                    messagebox.showwarning("تنبيه", "لا توجد مرفقات متاحة للمعاينة", parent=report_win)
                    return
                
                file_path = attachments_list[index]
                file_extension = os.path.splitext(file_path)[1].lower()
                
                # فحص أن الملف موجود
                if not os.path.exists(file_path):
                    messagebox.showerror("خطأ", f"الملف غير موجود:\n{file_path}", parent=report_win)
                    return
                
                # معاينة الصور فقط
                if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg']:
                    try:
                        import PIL.Image
                        from PIL import ImageTk
                        
                        # فتح الصورة
                        image = PIL.Image.open(file_path)
                        
                        # إنشاء نافذة معاينة
                        preview_win = tk.Toplevel(report_win)
                        preview_win.title(f"معاينة: {os.path.basename(file_path)}")
                        preview_win.geometry("700x600")
                        preview_win.configure(bg="#2e2e2e")
                        
                        # إطار العنوان
                        title_frame = tk.Frame(preview_win, bg="#2e2e2e")
                        title_frame.pack(fill="x", padx=10, pady=5)
                        
                        tk.Label(title_frame, text=f"معاينة: {os.path.basename(file_path)}", 
                                bg="#2e2e2e", fg="white", font=("SegoeUI", 12, "bold")).pack()
                        
                        # إطار الصورة
                        image_frame = tk.Frame(preview_win, bg="#2e2e2e")
                        image_frame.pack(expand=True, fill="both", padx=10, pady=5)
                        
                        # تحجيم الصورة إذا كانت كبيرة
                        max_size = (650, 450)
                        image.thumbnail(max_size, PIL.Image.Resampling.LANCZOS)
                        
                        # عرض الصورة
                        photo = ImageTk.PhotoImage(image)
                        image_label = tk.Label(image_frame, image=photo, bg="#2e2e2e")
                        image_label.image = photo  # حفظ مرجع للصورة
                        image_label.pack(expand=True)
                        
                        # معلومات الملف
                        info_frame = tk.Frame(preview_win, bg="#2e2e2e")
                        info_frame.pack(fill="x", padx=10, pady=5)
                        
                        file_size = os.path.getsize(file_path)
                        file_size_mb = file_size / (1024 * 1024)
                        
                        # معلومات إضافية عن الصورة
                        width, height = image.size
                        mode = image.mode
                        
                        info_text = f"اسم الملف: {os.path.basename(file_path)}\n"
                        info_text += f"الحجم: {file_size_mb:.2f} ميجابايت\n"
                        info_text += f"الأبعاد: {width} × {height} بكسل\n"
                        info_text += f"النوع: {file_extension.upper()}\n"
                        info_text += f"نمط اللون: {mode}"
                        
                        tk.Label(info_frame, text=info_text, bg="#2e2e2e", fg="white", 
                                font=("SegoeUI", 10), justify="right").pack()
                        
                        # أزرار إضافية
                        btn_frame = tk.Frame(preview_win, bg="#2e2e2e")
                        btn_frame.pack(fill="x", padx=10, pady=5)
                        
                        def optimize_image():
                            """تحسين الصورة (تقليل الحجم)"""
                            try:
                                # حفظ نسخة محسنة
                                optimized_path = file_path.replace(file_extension, f"_optimized{file_extension}")
                                
                                if file_extension in ['.jpg', '.jpeg']:
                                    image.save(optimized_path, 'JPEG', quality=85, optimize=True)
                                elif file_extension == '.png':
                                    image.save(optimized_path, 'PNG', optimize=True)
                                else:
                                    image.save(optimized_path)
                                
                                optimized_size = os.path.getsize(optimized_path)
                                optimized_size_mb = optimized_size / (1024 * 1024)
                                
                                savings = ((file_size - optimized_size) / file_size) * 100
                                
                                messagebox.showinfo("تم التحسين", 
                                    f"تم حفظ نسخة محسنة:\n{os.path.basename(optimized_path)}\n\n"
                                    f"الحجم الأصلي: {file_size_mb:.2f} ميجابايت\n"
                                    f"الحجم المحسن: {optimized_size_mb:.2f} ميجابايت\n"
                                    f"التوفير: {savings:.1f}%", 
                                    parent=preview_win)
                                
                            except Exception as e:
                                messagebox.showerror("خطأ", f"فشل في تحسين الصورة: {str(e)}", parent=preview_win)
                        
                        tk.Button(btn_frame, text="تحسين الصورة", command=optimize_image,
                                 bg="#4CAF50", fg="white", font=("SegoeUI", 9)).pack(side="left", padx=2)
                        
                    except ImportError:
                        messagebox.showwarning("تنبيه", "مكتبة PIL مطلوبة لمعاينة الصور", parent=report_win)
                    except Exception as e:
                        messagebox.showerror("خطأ", f"فشل في معاينة الصورة: {str(e)}", parent=report_win)
                else:
                    messagebox.showinfo("معلومات", "المعاينة متاحة للصور فقط", parent=report_win)
            
            # أزرار إدارة المرفقات
            attachment_btn_frame = tk.Frame(attachment_frame, bg="#2e2e2e")
            attachment_btn_frame.pack(fill="x", pady=5)
            
            # إنشاء الأزرار مع مراجع لها
            add_btn = tk.Button(attachment_btn_frame, text="إضافة مرفق", command=add_attachment,
                     bg="#4CAF50", fg="white", font=("SegoeUI", 10))
            add_btn.pack(side="left", padx=2)
            
            preview_btn = tk.Button(attachment_btn_frame, text="معاينة", command=preview_attachment,
                     bg="#2196F3", fg="white", font=("SegoeUI", 10))
            preview_btn.pack(side="left", padx=2)
            
            remove_btn = tk.Button(attachment_btn_frame, text="إزالة مرفق", command=remove_attachment,
                     bg="#f44336", fg="white", font=("SegoeUI", 10))
            remove_btn.pack(side="left", padx=2)
            
            clear_btn = tk.Button(attachment_btn_frame, text="مسح الكل", command=clear_attachments,
                     bg="#ff9800", fg="white", font=("SegoeUI", 10))
            clear_btn.pack(side="left", padx=2)
            
            # تعطيل الأزرار في البداية
            preview_btn.config(state="disabled")
            remove_btn.config(state="disabled")
            clear_btn.config(state="disabled")
            
            def update_buttons_state():
                """تحديث حالة الأزرار بناءً على وجود مرفقات"""
                has_attachments = len(attachments_list) > 0
                has_selection = len(attachments_listbox.curselection()) > 0
                
                preview_btn.config(state="normal" if has_selection else "disabled")
                remove_btn.config(state="normal" if has_selection else "disabled")
                clear_btn.config(state="normal" if has_attachments else "disabled")
            
            # ربط حدث اختيار المرفق بتحديث حالة الأزرار
            attachments_listbox.bind('<<ListboxSelect>>', lambda e: update_buttons_state())
            
            # تحديث حالة الأزرار عند إضافة/إزالة مرفقات
            original_add_attachment = add_attachment
            original_remove_attachment = remove_attachment
            original_clear_attachments = clear_attachments
            
            def add_attachment_with_update():
                original_add_attachment()
                update_buttons_state()
            
            def remove_attachment_with_update():
                original_remove_attachment()
                update_buttons_state()
            
            def clear_attachments_with_update():
                original_clear_attachments()
                update_buttons_state()
            
            # تحديث الأزرار لاستخدام الدوال المحدثة
            add_btn.config(command=add_attachment_with_update)
            remove_btn.config(command=remove_attachment_with_update)
            clear_btn.config(command=clear_attachments_with_update)

            # إطار للأزرار
            btn_frame = tk.Frame(report_win, bg="#2e2e2e")
            btn_frame.pack(fill="x", padx=10, pady=10)

            def send_via_email():
                nonlocal selected, attachments_list
                message = report_text.get("1.0", tk.END).strip()
                if not message:
                    messagebox.showwarning("تنبيه", "يرجى إدخال نص التقرير.", parent=report_win)
                    return

                # إعداد رسالة التأكيد
                confirm_msg = f"سيتم إرسال التقرير إلى {len(selected)} طالب عبر Gmail."
                if attachments_list:
                    attachment_names = [os.path.basename(att) for att in attachments_list]
                    confirm_msg += f"\n\nالمرفقات:\n" + "\n".join([f"• {name}" for name in attachment_names])
                
                confirm_msg += "\n\nهل تريد المتابعة؟"
                
                # عرض تأكيد مع عدد الطلاب المحددين والمرفقات
                confirm = messagebox.askyesno(
                    "تأكيد الإرسال",
                    confirm_msg,
                    parent=report_win
                )

                if confirm:
                    success_count = 0
                    failed_count = 0
                    
                    for student in selected:
                        try:
                            if not student['البريد']:
                                messagebox.showwarning("تنبيه", 
                                    f"البريد الإلكتروني غير متوفر للطالب {student['الاسم']}. يرجى إضافته أولاً.",
                                    parent=report_win)
                                continue

                            send_email(
                                to_address=student['البريد'],
                                subject="تقرير عن الطالب   -تسجيل حضور أو غياب او تقارير الطالب عند أستاذ علي أبو بكر " + student['الاسم'],
                                body=message,
                                attachments=attachments_list if attachments_list else None
                            )
                            success_count += 1
                        except Exception as e:
                            print(f"فشل في الإرسال إلى {student['الاسم']}: {e}")
                            failed_count += 1

                    # إعداد رسالة النتيجة
                    if failed_count == 0:
                        result_msg = f"تم إرسال التقارير بنجاح إلى {success_count} أولياء أمور."
                        if attachments_list:
                            result_msg += f"\n\nتم إرفاق {len(attachments_list)} ملف مع كل تقرير."
                        messagebox.showinfo("تم", result_msg, parent=report_win)
                    else:
                        result_msg = f"تم إرسال {success_count} تقرير بنجاح.\nفشل إرسال {failed_count} تقرير."
                        if attachments_list:
                            result_msg += f"\n\nتم إرفاق {len(attachments_list)} ملف مع التقارير المرسلة بنجاح."
                        messagebox.showwarning("تنبيه", result_msg, parent=report_win)
                    report_win.destroy()

            def send_via_whatsapp():
                nonlocal selected, attachments_list
                message = report_text.get("1.0", tk.END).strip()
                if not message:
                    messagebox.showwarning("تنبيه", "يرجى إدخال نص التقرير.", parent=report_win)
                    return
                
                # تنبيه حول المرفقات
                if attachments_list:
                    # فحص صيغ الملفات المدعومة
                    supported_formats = [
                        '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.zip', '.rar', '.7z',
                        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg',
                        '.txt'
                    ]
                    unsupported_files = []
                    supported_files = []
                    
                    for file_path in attachments_list:
                        file_ext = os.path.splitext(file_path.lower())[1]
                        if file_ext in supported_formats:
                            supported_files.append(file_path)
                        else:
                            unsupported_files.append(file_path)
                    
                    if unsupported_files:
                        warning_msg = "تنبيه: بعض الملفات غير مدعومة في الواتساب.\n\n"
                        warning_msg += "الملفات المدعومة:\n"
                        for file_path in supported_files:
                            warning_msg += f"✅ {os.path.basename(file_path)}\n"
                        warning_msg += "\nالملفات غير المدعومة:\n"
                        for file_path in unsupported_files:
                            warning_msg += f"❌ {os.path.basename(file_path)}\n"
                        warning_msg += "\nملاحظة: جميع أنواع الملفات مدعومة"
                        warning_msg += "\n\nهل تريد المتابعة مع الملفات المدعومة فقط؟"
                        
                        if not messagebox.askyesno("تنبيه حول الملفات", warning_msg, parent=report_win):
                            return
                        
                        # استخدام الملفات المدعومة فقط
                        attachments_list[:] = supported_files
                    
                    if not attachments_list:
                        messagebox.showwarning("تنبيه", "لا توجد ملفات مدعومة لإرسالها عبر الواتساب.", parent=report_win)
                        return

                # تجهيز قائمة الطلاب الذين لديهم أرقام هواتف صالحة
                valid_students = [student for student in selected if student.get('الهاتف') and str(student['الهاتف']).strip() != "nan"]
                

                if not valid_students:
                    messagebox.showwarning("تنبيه", "لا توجد أرقام هواتف صالحة للإرسال إليها.", parent=report_win)
                    return

                # حساب عدد الدفعات والوقت المتوقع
                total_messages = len(valid_students)
                batch_size = 60
                delay_minutes = 1
                estimated_batches = (total_messages + batch_size - 1) // batch_size
                estimated_time = (estimated_batches - 1) * delay_minutes
                confirm_msg = f"سيتم إرسال {total_messages} رسالة على {estimated_batches} دفعة.\n"
                confirm_msg += f"الوقت المتوقع: حوالي {estimated_time} دقيقة."
                
                # إضافة معلومات عن المرفقات
                if attachments_list:
                    attachment_names = [os.path.basename(att) for att in attachments_list]
                    confirm_msg += f"\n\n📎 المرفقات المرفقة:\n" + "\n".join([f"📄 {name}" for name in attachment_names])
                    confirm_msg += "\n\n✅ ملاحظة:"
                    confirm_msg += "\n• المرفقات ستُرسل فعلياً عبر الواتساب"
                    confirm_msg += "\n• جميع أنواع الملفات مدعومة (صور، مستندات، ملفات مضغوطة)"
                    confirm_msg += "\n• سيتم إرسال كل ملف مع رسالة نصية"
                
                confirm_msg += "\n\nهل تريد المتابعة؟"

                # عرض تأكيد مع عدد الطلاب المحددين والدفعات
                confirm = messagebox.askyesno(
                    "تأكيد الإرسال",
                    confirm_msg,
                    parent=report_win
                )

                if confirm:
                    def create_message(student):
                        
                        base_message = f"تقرير عن الطالب {student['الاسم']}\n\n{message}\n\n{{-تسجيل حضور أو غياب او تقارير الطالب عند أستاذ علي أبو بكر }}"
                        
                        # إضافة معلومات عن المرفقات إذا وجدت
                        if attachments_list:
                            attachment_names = [os.path.basename(att) for att in attachments_list]
                            attachment_info = f"\n\n📎 المرفقات المرفقة:\n" + "\n".join([f"📄 {name}" for name in attachment_names])
                            base_message += attachment_info
                            base_message += "\n\n✅ ملاحظة:"
                            base_message += "\n• المرفقات ستُرسل فعلياً مع هذه الرسالة"
                            base_message += "\n• جميع أنواع الملفات مدعومة (صور، مستندات، ملفات مضغوطة)"
                            base_message += "\n• سيتم إرسال كل ملف منفصلاً"
                        
                        return base_message

                    try:
                        success_count, failed_count, failed_msgs = send_whatsapp_batch(
                            valid_students,
                            create_message,
                            batch_size=batch_size,
                            delay_minutes=delay_minutes,
                            attachments=attachments_list if attachments_list else None
                        )
                        if failed_count == 0:
                            result_msg = f"تم إرسال التقارير بنجاح إلى {success_count} أولياء أمور."
                            if attachments_list:
                                result_msg += f"\n\nتم إرسال {len(attachments_list)} مرفق فعلياً مع كل تقرير."
                                # إضافة معلومات عن أنواع الملفات
                                image_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg'])
                                doc_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.pdf', '.doc', '.docx'])
                                excel_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.xls', '.xlsx'])
                                archive_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.zip', '.rar', '.7z'])
                                other_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.txt'])
                                
                                if image_count > 0:
                                    result_msg += f"\n🖼️ {image_count} صورة"
                                if doc_count > 0:
                                    result_msg += f"\n📄 {doc_count} مستند"
                                if excel_count > 0:
                                    result_msg += f"\n📊 {excel_count} ملف Excel"
                                if archive_count > 0:
                                    result_msg += f"\n📦 {archive_count} ملف مضغوط"
                                if other_count > 0:
                                    result_msg += f"\n📝 {other_count} ملف نصي"
                            messagebox.showinfo("تم", result_msg, parent=report_win)
                        else:
                            # إنشاء نافذة منبثقة لعرض الأخطاء مع زر إعادة المحاولة
                            error_win = tk.Toplevel(report_win)
                            error_win.title("نتيجة الإرسال")
                            error_win.geometry("600x400")
                            error_win.configure(bg="#2e2e2e")
                            
                            # إطار للرسالة الرئيسية
                            main_frame = tk.Frame(error_win, bg="#2e2e2e")
                            main_frame.pack(fill="x", padx=10, pady=10)
                            
                            result_text = f"تم إرسال {success_count} تقرير غياب بنجاح.\nفشل إرسال {failed_count} تقرير."
                            if attachments_list:
                                result_text += f"\n\nتم إرسال {len(attachments_list)} مرفق فعلياً مع التقارير المرسلة بنجاح."
                                # إضافة معلومات عن أنواع الملفات
                                image_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.svg'])
                                doc_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.pdf', '.doc', '.docx'])
                                excel_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.xls', '.xlsx'])
                                archive_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.zip', '.rar', '.7z'])
                                other_count = sum(1 for att in attachments_list if os.path.splitext(att.lower())[1] in ['.txt'])
                                
                                if image_count > 0:
                                    result_text += f"\n🖼️ {image_count} صورة"
                                if doc_count > 0:
                                    result_text += f"\n📄 {doc_count} مستند"
                                if excel_count > 0:
                                    result_text += f"\n📊 {excel_count} ملف Excel"
                                if archive_count > 0:
                                    result_text += f"\n📦 {archive_count} ملف مضغوط"
                                if other_count > 0:
                                    result_text += f"\n📝 {other_count} ملف نصي"
                            tk.Label(main_frame, text=result_text, bg="#2e2e2e", fg="white", 
                                   font=("Helvetica", 12, "bold")).pack(pady=10)
                            
                            # إطار لقائمة الطلاب الفاشلين
                            list_frame = tk.Frame(error_win, bg="#2e2e2e")
                            list_frame.pack(fill="both", expand=True, padx=10, pady=5)
                            
                            tk.Label(list_frame, text="الطلاب الذين فشل إرسال التقارير إليهم:", 
                                   bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
                            
                            # إنشاء قائمة للطلاب الفاشلين
                            failed_listbox = tk.Listbox(list_frame, font=("Helvetica", 11), height=10)
                            failed_listbox.pack(fill="both", expand=True)
                            
                            # إضافة شريط التمرير
                            scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=failed_listbox.yview)
                            scrollbar.pack(side="right", fill="y")
                            failed_listbox.configure(yscrollcommand=scrollbar.set)
                            
                            # استخراج أسماء الطلاب الفاشلين من رسائل الأخطاء
                            failed_student_names = []
                            for msg in failed_msgs:
                                if ":" in msg:
                                    student_name = msg.split(":")[0].strip()
                                    failed_student_names.append(student_name)
                                    failed_listbox.insert(tk.END, student_name)
                            
                            # إطار للأزرار
                            btn_frame = tk.Frame(error_win, bg="#2e2e2e")
                            btn_frame.pack(fill="x", padx=10, pady=10)
                            
                            def retry_failed_students():
                                """إعادة المحاولة للطلاب الفاشلين فقط"""
                                if not failed_student_names:
                                    messagebox.showwarning("تنبيه", "لا يوجد طلاب لإعادة المحاولة.", parent=error_win)
                                    return
                                
                                # فلترة السجلات للطلاب الفاشلين فقط
                                retry_records = [record for record in valid_students 
                                               if record["الاسم"] in failed_student_names]
                                
                                if not retry_records:
                                    messagebox.showwarning("تنبيه", "لا توجد بيانات صالحة للطلاب الفاشلين.", parent=error_win)
                                    return
                                
                                # عرض رسالة تأكيد
                                retry_msg = f"سيتم إعادة المحاولة لـ {len(retry_records)} طالب."
                                if attachments_list:
                                    retry_msg += f"\n\nسيتم إرسال {len(attachments_list)} مرفق فعلياً مع كل تقرير."
                                retry_msg += "\n\nهل تريد المتابعة؟"
                                if not messagebox.askyesno("تأكيد إعادة المحاولة", retry_msg, parent=error_win):
                                    return
                                
                                try:
                                    # إعادة المحاولة
                                    retry_success, retry_failed, retry_failed_msgs = send_whatsapp_batch(
                                        retry_records,
                                        create_message,
                                        batch_size=30,  # دفعة أصغر لإعادة المحاولة
                                        delay_minutes=2,  # انتظار أطول
                                        attachments=attachments_list if attachments_list else None
                                    )
                                    
                                    if retry_failed == 0:
                                        result_msg = f"تم إرسال جميع التقارير بنجاح بعد إعادة المحاولة."
                                        if attachments_list:
                                            result_msg += f"\n\nتم إرسال {len(attachments_list)} مرفق فعلياً مع كل تقرير."
                                        messagebox.showinfo("تم", result_msg, parent=error_win)
                                        error_win.destroy()
                                    else:
                                        result_msg = f"تم إرسال {retry_success} تقرير بنجاح.\nفشل إرسال {retry_failed} تقرير بعد إعادة المحاولة."
                                        if attachments_list:
                                            result_msg += f"\n\nتم إرسال {len(attachments_list)} مرفق فعلياً مع التقارير المرسلة بنجاح."
                                        messagebox.showwarning("تنبيه", result_msg, parent=error_win)
                                    
                                except Exception as e:
                                    messagebox.showerror("خطأ", f"حدث خطأ أثناء إعادة المحاولة: {str(e)}", parent=error_win)
                                
                            # أزرار التحكم
                            retry_btn = tk.Button(btn_frame, text="إعادة المحاولة للطلاب الفاشلين", 
                                                command=retry_failed_students, bg="#ffaa00", fg="black", 
                                                font=("Helvetica", 12))
                            retry_btn.pack(side="left", padx=5)
                            
                            close_btn = tk.Button(btn_frame, text="إغلاق", command=error_win.destroy,
                                               bg="#cc3333", fg="white", font=("Helvetica", 12))
                            close_btn.pack(side="right", padx=5)
                            
                            # جعل النافذة في المنتصف
                            error_win.transient(report_win)
                            error_win.grab_set()
                            
                    except Exception as e:
                        messagebox.showerror("خطأ", f"حدث خطأ أثناء الإرسال: {str(e)}", parent=report_win)
                    
                    report_win.destroy()

            # أزرار الإرسال
            def test_gmail_button():
                print("تم الضغط على زر Gmail")
                send_via_email()
            
            def test_whatsapp_button():
                print("تم الضغط على زر WhatsApp")
                send_via_whatsapp()
            
            tk.Button(btn_frame, text="إرسال عبر Gmail", command=test_gmail_button,
                     bg="#00cc66", fg="white", font=("Helvetica", 12)).pack(side="left", padx=5)

            tk.Button(btn_frame, text="إرسال عبر WhatsApp", command=test_whatsapp_button,
                     bg="#25D366", fg="white", font=("Helvetica", 12)).pack(side="left", padx=5)

            tk.Button(btn_frame, text="إلغاء", command=report_win.destroy,
                     bg="#cc3333", fg="white", font=("Helvetica", 12)).pack(side="left", padx=5)

            # جعل النافذة في المنتصف
            report_win.transient(win)
            report_win.grab_set()
            win.wait_window(report_win)

        def edit_student():
            selected = get_selected_students()
            if len(selected) != 1:
                messagebox.showwarning("تنبيه", "يرجى تحديد طالب واحد فقط للتعديل.")
                return

            student_data = selected[0]
            student_index = student_data["index"]  # استخدم الـ index مباشرة

            # الحصول على المجموعة الحالية للطالب
            current_group = self.students.at[student_index, "المجموعة"]

            edit_win = tk.Toplevel(win)
            edit_win.title("تعديل بيانات الطالب")
            edit_win.geometry("400x500")
            edit_win.configure(bg="#2e2e2e")

            tk.Label(edit_win, text="اسم الطالب:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack()
            name_entry = tk.Entry(edit_win, font=("Helvetica", 12))
            add_copy_paste_support(name_entry)
            name_entry.insert(0, student_data["الاسم"])
            name_entry.pack()

            tk.Label(edit_win, text="الصف:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack()
            grade_entry = ttk.Combobox(edit_win, values=["الصف الأول الثانوي", "الصف الثاني الثانوي", "الصف الثالث الثانوي"], 
                                     font=("Helvetica", 12), state="readonly")
            grade_entry.set(student_data["الصف"])
            grade_entry.pack()

            tk.Label(edit_win, text="البريد:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack()
            email_entry = tk.Entry(edit_win, font=("Helvetica", 12))
            add_copy_paste_support(email_entry)
            email_entry.insert(0, student_data["البريد"])
            email_entry.pack()

            tk.Label(edit_win, text="رقم الهاتف:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack()
            phone_entry = tk.Entry(edit_win, font=("Helvetica", 12))
            add_copy_paste_support(phone_entry)
            phone_entry.insert(0, student_data.get("الهاتف", ""))
            phone_entry.pack()

            tk.Label(edit_win, text="المجموعة:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack()
            group_entry = ttk.Combobox(edit_win, values=self.groups["المجموعة"].tolist(), 
                                     font=("Helvetica", 12), state="readonly")
            group_entry.set(current_group)
            group_entry.pack()

            def save_changes():
                self.students.at[student_index, "الاسم"] = name_entry.get().strip()
                self.students.at[student_index, "الصف"] = grade_entry.get().strip()
                self.students.at[student_index, "البريد"] = email_entry.get().strip()
                self.students.at[student_index, "الهاتف"] = phone_entry.get().strip()
                self.students.at[student_index, "المجموعة"] = group_entry.get().strip()
                self.students.to_csv(STUDENT_FILE, index=False, encoding='utf-8-sig', sep=';')
                edit_win.destroy()
                show_students(None)
                messagebox.showinfo("تم", "تم تعديل بيانات الطالب.")

            tk.Button(edit_win, text="حفظ التعديلات", command=save_changes, 
                     bg="#00cc66", fg="white", font=("Helvetica", 12)).pack(pady=10)

        # تحديث أزرار التحكم
        control_frame = tk.Frame(win, bg="#2e2e2e")
        control_frame.pack(fill="x", padx=10, pady=5)

        edit_btn = tk.Button(control_frame, text="تعديل بيانات الطالب", command=edit_student, 
                           bg="#cccc00", fg="black", font=("Helvetica", 12))
        edit_btn.pack(side="left", padx=5)

        def transfer_students():
            selected = get_selected_students()
            if not selected:
                messagebox.showwarning("تنبيه", "يرجى تحديد طلاب للترحيل.", parent=win)
                return

            # إنشاء نافذة منبثقة لاختيار المجموعة الهدف
            transfer_win = tk.Toplevel(win)
            transfer_win.title("ترحيل الطلاب")
            transfer_win.geometry("400x200")
            transfer_win.configure(bg="#2e2e2e")

            # الحصول على المجموعة الحالية
            sel = group_listbox.curselection()
            if not sel:
                messagebox.showwarning("تنبيه", "يرجى اختيار مجموعة المصدر أولاً.", parent=win)
                return
            current_group = group_listbox.get(sel[0]).split(" - ")[0]

            # إنشاء قائمة المجموعات المتاحة (باستثناء المجموعة الحالية)
            available_groups = [g for g in self.groups["المجموعة"].tolist() if g != current_group]
            if not available_groups:
                messagebox.showwarning("تنبيه", "لا توجد مجموعات أخرى متاحة للترحيل.", parent=win)
                return

            tk.Label(transfer_win, text="اختر المجموعة الهدف:", bg="#2e2e2e", fg="white", 
                    font=("Helvetica", 12)).pack(pady=10)
            
            target_group_var = tk.StringVar()
            target_group_combo = ttk.Combobox(transfer_win, textvariable=target_group_var,
                                            values=available_groups, state="readonly",
                                            font=("Helvetica", 12))
            target_group_combo.pack(pady=10)

            def confirm_transfer():
                target_group = target_group_var.get()
                if not target_group:
                    messagebox.showwarning("تنبيه", "يرجى اختيار مجموعة الهدف.", parent=transfer_win)
                    return

                confirm = messagebox.askyesno(
                    "تأكيد الترحيل",
                    f"هل أنت متأكد من ترحيل {len(selected)} طالب من مجموعة '{current_group}' إلى مجموعة '{target_group}'؟",
                    parent=transfer_win
                )

                if confirm:
                    # تحديث مجموعة الطلاب المحددين
                    for student in selected:
                        student_index = student["index"]
                        self.students.at[student_index, "المجموعة"] = target_group

                    # حفظ التغييرات
                    self.students.to_csv(STUDENT_FILE, index=False, encoding='utf-8-sig', sep=';')
                    
                    # تحديث العرض
                    show_students(None)
                    transfer_win.destroy()
                    messagebox.showinfo("تم", f"تم ترحيل {len(selected)} طالب بنجاح إلى مجموعة '{target_group}'.", parent=win)

            tk.Button(transfer_win, text="تأكيد الترحيل", command=confirm_transfer,
                     bg="#00cc66", fg="white", font=("Helvetica", 12)).pack(pady=10)

        transfer_btn = tk.Button(control_frame, text="ترحيل الطلاب", command=transfer_students,
                               bg="#9933ff", fg="white", font=("SegoeUI", 12))
        transfer_btn.pack(side="left", padx=5)

        send_email_btn = tk.Button(control_frame, text="إرسال تقارير عبر Gmail", command=send_reports, 
                           bg="#00bfff", fg="white", font=("SegoeUI", 12))
        send_email_btn.pack(side="left", padx=5)

        send_whatsapp_btn = tk.Button(control_frame, text="إرسال تقارير عبر WhatsApp", command=send_reports, 
                           bg="#25D366", fg="white", font=("SegoeUI", 12))
        send_whatsapp_btn.pack(side="left", padx=5)

        def delete_students():
            selected = get_selected_students()
            if not selected:
                messagebox.showwarning("تنبيه", "يرجى تحديد طلاب لحذفهم.", parent=win)
                return
            confirm = messagebox.askyesno("تأكيد الحذف", f"هل أنت متأكد أنك تريد حذف {len(selected)} طالب؟", parent=win)
            if not confirm:
                return
            # حذف الطلاب باستخدام الـ index
            indices = [student["index"] for student in selected]
            self.students = self.students.drop(indices)
            self.students.to_csv(STUDENT_FILE, index=False, encoding='utf-8-sig', sep=';')
            show_students(None)
            messagebox.showinfo("تم", "تم حذف الطلاب المحددين.", parent=win)

        delete_btn = tk.Button(control_frame, text="حذف الطلاب", command=delete_students, 
                           bg="#cc3333", fg="white", font=("SegoeUI", 12))
        delete_btn.pack(side="left", padx=5)

        # إضافة زر تسجيل الغياب
        attendance_btn = tk.Button(control_frame, text="تسجيل الغياب", 
                               command=lambda: self.open_attendance_window(win, group_listbox), 
                               bg="#ffaa00", fg="black", font=("SegoeUI", 12))
        attendance_btn.pack(side="left", padx=5)

    # نقل تعريف الدالة خارج view_groups_with_checkboxes
    def open_attendance_window(self, parent_win, group_listbox):
        sel = group_listbox.curselection()
        if not sel:
            messagebox.showwarning("تنبيه", "يرجى اختيار مجموعة أولاً.", parent=parent_win)
            return
        group_info = group_listbox.get(sel[0])
        group_name = group_info.split(" - ")[0]
        group_students = self.students[self.students["المجموعة"] == group_name]

        att_win = tk.Toplevel(parent_win)
        att_win.title(f"تسجيل الغياب - {group_name}")
        att_win.geometry("800x600")
        att_win.configure(bg="#2e2e2e")

        # إطار اختيار الحصة والتاريخ
        filter_frame = tk.Frame(att_win, bg="#2e2e2e")
        filter_frame.pack(fill="x", padx=10, pady=5)

        # اختيار الحصة
        lesson_frame = tk.Frame(filter_frame, bg="#2e2e2e")
        lesson_frame.pack(side="left", padx=10)
        
        tk.Label(lesson_frame, text="اختر الحصة:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
        lesson_var = tk.StringVar()
        # إنشاء قائمة الحصص مع الوقت للتمييز بين الحصص المتشابهة
        lesson_values = []
        for _, row in self.lessons.iterrows():
            lesson_name = row["الحصة"]
            lesson_time = row["الوقت"]
            lesson_values.append(f"{lesson_name} - {lesson_time}")
        
        lesson_combo = ttk.Combobox(lesson_frame, textvariable=lesson_var, 
                                  values=lesson_values, 
                                  state="readonly", font=("SegoeUI", 12))
        lesson_combo.pack(side="left", padx=5)

        def add_new_lesson():
            add_win = tk.Toplevel(att_win)
            add_win.title("إضافة حصة جديدة")
            add_win.geometry("400x350")
            add_win.configure(bg="#2e2e2e")

            # إضافة خيار لاختيار نوع الحصة
            lesson_type_frame = tk.Frame(add_win, bg="#2e2e2e")
            lesson_type_frame.pack(fill="x", padx=10, pady=5)
            
            lesson_type_var = tk.StringVar(value="custom")
            
            def update_lesson_type():
                if lesson_type_var.get() == "default":
                    # تعطيل حقول الإدخال عند اختيار الحصص الافتراضية
                    lesson_entry.configure(state="disabled")
                    time_entry.configure(state="disabled")
                    desc_entry.configure(state="disabled")
                else:
                    # تفعيل حقول الإدخال عند اختيار حصة مخصصة
                    lesson_entry.configure(state="normal")
                    time_entry.configure(state="normal")
                    desc_entry.configure(state="normal")

            tk.Radiobutton(lesson_type_frame, text="حصة مخصصة", variable=lesson_type_var, 
                         value="custom", command=update_lesson_type,
                         bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
            
            tk.Radiobutton(lesson_type_frame, text="حصة افتراضية", variable=lesson_type_var,
                         value="default", command=update_lesson_type,
                         bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)

            # إطار الحصص الافتراضية
            default_lesson_frame = tk.Frame(add_win, bg="#2e2e2e")
            default_lesson_frame.pack(fill="x", padx=10, pady=5)
            
            tk.Label(default_lesson_frame, text="اختر الحصة الافتراضية:", 
                    bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            
            default_lesson_var = tk.StringVar()
            default_lessons = [
                ("حصة 1", "08:00 - 08:45", "الحصة الأولى"),
                ("حصة 2", "08:45 - 09:30", "الحصة الثانية"),
                ("حصة 3", "09:30 - 10:15", "الحصة الثالثة"),
                ("حصة 4", "10:15 - 11:00", "الحصة الرابعة"),
                ("حصة 5", "11:00 - 11:45", "الحصة الخامسة"),
                ("حصة 6", "11:45 - 12:30", "الحصة السادسة"),
                ("حصة 7", "12:30 - 13:15", "الحصة السابعة"),
                ("حصة 8", "13:15 - 14:00", "الحصة الثامنة")
            ]
            default_lesson_combo = ttk.Combobox(default_lesson_frame, textvariable=default_lesson_var,
                                              values=[lesson[0] for lesson in default_lessons],
                                              state="readonly", font=("SegoeUI", 12))
            default_lesson_combo.pack(pady=5)
            default_lesson_combo.configure(state="disabled")

            def update_default_lesson(*args):
                selected = default_lesson_var.get()
                if selected:
                    for lesson in default_lessons:
                        if lesson[0] == selected:
                            lesson_entry.delete(0, tk.END)
                            lesson_entry.insert(0, lesson[0])
                            time_entry.delete(0, tk.END)
                            time_entry.insert(0, lesson[1])
                            desc_entry.delete(0, tk.END)
                            desc_entry.insert(0, lesson[2])
                            break

            default_lesson_var.trace_add('write', update_default_lesson)

            # حقول إدخال الحصة المخصصة
            tk.Label(add_win, text="اسم الحصة:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(pady=5)
            lesson_entry = tk.Entry(add_win, font=("SegoeUI", 12))
            add_copy_paste_support(lesson_entry)
            lesson_entry.pack(pady=5)

            tk.Label(add_win, text="الوقت:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(pady=5)
            time_entry = tk.Entry(add_win, font=("SegoeUI", 12))
            add_copy_paste_support(time_entry)
            time_entry.pack(pady=5)

            tk.Label(add_win, text="الوصف:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(pady=5)
            desc_entry = tk.Entry(add_win, font=("SegoeUI", 12))
            add_copy_paste_support(desc_entry)
            desc_entry.pack(pady=5)

            def save_lesson():
                if lesson_type_var.get() == "default":
                    lesson = default_lesson_var.get()
                    if not lesson:
                        messagebox.showwarning("تنبيه", "يرجى اختيار حصة افتراضية.", parent=add_win)
                        return
                else:
                    lesson = lesson_entry.get().strip()
                    time = time_entry.get().strip()
                    desc = desc_entry.get().strip()

                    if not (lesson and time):
                        messagebox.showwarning("تنبيه", "يرجى ملء اسم الحصة والوقت.", parent=add_win)
                        return

                # تم إزالة التحقق من تكرار اسم الحصة للسماح بإضافة حصص بنفس الاسم

                try:
                    if lesson_type_var.get() == "default":
                        # إضافة الحصة الافتراضية المختارة
                        for default_lesson in default_lessons:
                            if default_lesson[0] == lesson:
                                new_row = pd.DataFrame({
                                    "الحصة": [default_lesson[0]],
                                    "الوقت": [default_lesson[1]],
                                    "الوصف": [default_lesson[2]]
                                })
                                break
                    else:
                        # إضافة الحصة المخصصة
                        new_row = pd.DataFrame({
                            "الحصة": [lesson],
                            "الوقت": [time],
                            "الوصف": [desc]
                        })

                    self.lessons = pd.concat([self.lessons, new_row], ignore_index=True)
                    self.save_lessons()
                    
                    # تحديث قائمة الحصص في الكومبوبوكس
                    lesson_values = []
                    for _, row in self.lessons.iterrows():
                        lesson_name = row["الحصة"]
                        lesson_time = row["الوقت"]
                        lesson_values.append(f"{lesson_name} - {lesson_time}")
                    
                    lesson_combo['values'] = lesson_values
                    lesson_var.set(f"{lesson} - {time}")
                    
                    add_win.destroy()
                    messagebox.showinfo("تم", "تمت إضافة الحصة بنجاح.", parent=att_win)
                except Exception as e:
                    messagebox.showerror("خطأ", f"حدث خطأ أثناء حفظ الحصة: {str(e)}", parent=add_win)

            def update_fields_state(*args):
                if lesson_type_var.get() == "default":
                    default_lesson_combo.configure(state="readonly")
                    lesson_entry.configure(state="disabled")
                    time_entry.configure(state="disabled")
                    desc_entry.configure(state="disabled")
                else:
                    default_lesson_combo.configure(state="disabled")
                    lesson_entry.configure(state="normal")
                    time_entry.configure(state="normal")
                    desc_entry.configure(state="normal")

            lesson_type_var.trace_add('write', update_fields_state)
            update_fields_state()  # تحديث حالة الحقول عند بدء النافذة

            tk.Button(add_win, text="حفظ", command=save_lesson, bg="#00cc66", fg="white", 
                     font=("SegoeUI", 12)).pack(pady=10)

        # زر إضافة حصة جديدة
        add_lesson_btn = tk.Button(lesson_frame, text="+", command=add_new_lesson, 
                                 bg="#00cc66", fg="white", font=("SegoeUI", 12, "bold"),
                                 width=2)
        add_lesson_btn.pack(side="left", padx=5)

        # اختيار التاريخ
        date_frame = tk.Frame(filter_frame, bg="#2e2e2e")
        date_frame.pack(side="left", padx=10)
        
        tk.Label(date_frame, text="اختر التاريخ:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(side="left", padx=5)
        date_var = tk.StringVar()
        def pick_date():
            import tkcalendar
            cal_win = tk.Toplevel(att_win)
            cal_win.title("اختر التاريخ")
            cal = tkcalendar.Calendar(cal_win, selectmode='day', date_pattern='yyyy-mm-dd')
            cal.pack(padx=10, pady=10)
            def set_date():
                date_var.set(cal.get_date())
                cal_win.destroy()
            tk.Button(cal_win, text="اختيار", command=set_date).pack(pady=5)
        date_entry = tk.Entry(date_frame, textvariable=date_var, font=("Helvetica", 12), state="readonly")
        date_entry.pack(side="left", padx=5)
        tk.Button(date_frame, text="...", command=pick_date, font=("Helvetica", 10)).pack(side="left", pady=5)

        # عرض معلومات الحصة
        lesson_info_frame = tk.Frame(att_win, bg="#2e2e2e")
        lesson_info_frame.pack(fill="x", padx=10, pady=5)

        time_label = tk.Label(lesson_info_frame, text="", bg="#2e2e2e", fg="white", font=("Helvetica", 12))
        time_label.pack(side="left", padx=5)
        
        desc_label = tk.Label(lesson_info_frame, text="", bg="#2e2e2e", fg="white", font=("Helvetica", 12))
        desc_label.pack(side="left", padx=5)

        def update_lesson_info(*args):
            lesson_with_time = lesson_var.get()
            if lesson_with_time:
                # استخراج اسم الحصة من النص (الاسم - الوقت)
                lesson_name = lesson_with_time.split(" - ")[0]
                lesson_data = self.lessons[self.lessons["الحصة"] == lesson_name].iloc[0]
                time_label.config(text=f"الوقت: {lesson_data['الوقت']}")
                desc_label.config(text=f"الوصف: {lesson_data['الوصف']}")
            else:
                time_label.config(text="")
                desc_label.config(text="")

        lesson_var.trace_add('write', update_lesson_info)

        # جدول الطلاب
        table_frame = tk.Frame(att_win, bg="#2e2e2e")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        columns = ("name", "status")
        att_tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        att_tree.heading("name", text="اسم الطالب")
        att_tree.heading("status", text="الحالة")
        att_tree.column("name", width=200)
        att_tree.column("status", width=100)
        att_tree.pack(fill="both", expand=True)

        # دالة لعرض الغياب القديم عند اختيار الحصة والتاريخ
        def load_old_attendance(*args):
            # مسح الجدول
            for item in att_tree.get_children():
                att_tree.delete(item)
            lesson_with_time = lesson_var.get()
            date = date_var.get()
            
            # استخراج اسم الحصة من النص (الاسم - الوقت)
            lesson = lesson_with_time.split(" - ")[0] if lesson_with_time else ""
            # تحميل الغياب القديم لو موجود
            old_status = {}
            # تأكد من أن الملف موجود وغير فارغ قبل محاولة قراءته
            abs_file = "absences.csv"
            if lesson and date and os.path.exists(abs_file) and os.path.getsize(abs_file) > 0:
                try:
                    # تحديد الفاصلة الصحيحة عند القراءة
                    df = pd.read_csv(abs_file, encoding='utf-8-sig', sep=';')
                    
                    # التحقق من وجود الأعمدة المطلوبة قبل التصفية
                    if all(col in df.columns for col in ["المجموعة", "الحصة", "التاريخ"]):
                        df = df[(df["المجموعة"] == group_name) & (df["الحصة"] == lesson) & (df["التاريخ"] == date)]
                        for _, row in df.iterrows():
                            old_status[row["الاسم"]] = row["الحالة"]
                    else:
                        print(f"تحذير: ملف الغياب {abs_file} لا يحتوي على الأعمدة المتوقعة عند التحميل.")

                except Exception as e:
                    print(f"خطأ أثناء قراءة ملف الغياب عند التحميل: {e}")
                    # يمكن إضافة رسالة تنبيه للمستخدم هنا إذا أردت
                    pass # تجاهل الخطأ واستمر بدون تحميل بيانات الغياب

            # عرض جميع الطلاب في المجموعة مع الحالة القديمة أو حاضر افتراضيًا
            # نستخدم group_students التي تم تعريفها مرة واحدة عند فتح النافذة
            for _, row in group_students.iterrows():
                status = old_status.get(row["الاسم"], "حاضر")
                att_tree.insert("", "end", values=(row["الاسم"], status))

        # ربط تحميل الغياب القديم بتغيير الحصة أو التاريخ
        lesson_var.trace_add('write', load_old_attendance)
        date_var.trace_add('write', load_old_attendance)

        # أول تحميل للجدول
        load_old_attendance()

        # تعديل الحالة عند الضغط
        def toggle_status(event):
            item = att_tree.identify_row(event.y)
            if item:
                current = att_tree.item(item)['values']
                new_status = "غائب" if current[1] == "حاضر" else "حاضر"
                att_tree.item(item, values=(current[0], new_status))
        att_tree.bind("<Double-1>", toggle_status)

        # زر حفظ (مع الحفظ والإرسال)
        def save_attendance():
            lesson_with_time = lesson_var.get()
            date = date_var.get()
            if not lesson_with_time or not date:
                messagebox.showwarning("تنبيه", "يرجى اختيار الحصة والتاريخ.", parent=att_win)
                return
            
            # استخراج اسم الحصة من النص (الاسم - الوقت)
            lesson = lesson_with_time.split(" - ")[0]
            records = []
            for item in att_tree.get_children():
                name, status = att_tree.item(item)['values']
                # الحصول على بيانات الطالب من self.students
                # نستخدم group_students التي تم تعريفها مرة واحدة عند فتح النافذة
                student_row = group_students[group_students["الاسم"] == name].iloc[0]
                phone = student_row.get("الهاتف", "")
                group = group_name # تأكد أن group_name متاح من النطاق الخارجي
                record = {
                    "الاسم": name,
                    "المجموعة": group,
                    "الحصة": lesson,
                    "التاريخ": date,
                    "الحالة": status,
                    "الهاتف": phone
                }
                records.append(record)
            
            # حفظ في absences.csv (تحديث أو إضافة)
            abs_file = "absences.csv"
            # تأكد من تعريف الأعمدة المتوقعة
            expected_columns = ["الاسم", "المجموعة", "الحصة", "التاريخ", "الحالة", "الهاتف"]

            if os.path.exists(abs_file) and os.path.getsize(abs_file) > 0:
                try:
                    # تحديد الفاصلة الصحيحة عند القراءة
                    df = pd.read_csv(abs_file, encoding='utf-8-sig', sep=';')
                    
                    # التحقق من وجود الأعمدة المطلوبة
                    if all(col in df.columns for col in ["المجموعة", "الحصة", "التاريخ"]):
                        # حذف السجلات القديمة لنفس المجموعة/الحصة/التاريخ إذا كانت الأعمدة موجودة
                        mask = ~((df["المجموعة"] == group) & (df["الحصة"] == lesson) & (df["التاريخ"] == date))
                        df = df[mask]
                        # إضافة السجلات الجديدة
                        df = pd.concat([df, pd.DataFrame(records, columns=expected_columns)], ignore_index=True)
                    else:
                        # إذا كانت الأعمدة غير موجودة، نبدأ بـ DataFrame جديد فقط بالسجلات الجديدة
                        print(f"تحذير: ملف الغياب {abs_file} لا يحتوي على الأعمدة المتوقعة. سيتم إنشاء ملف جديد.")
                        df = pd.DataFrame(records, columns=expected_columns)
                        
                except Exception as e:
                    print(f"خطأ أثناء قراءة ملف الغياب عند الحفظ: {e}")
                    # في حالة وجود خطأ في الحفظ، نبدأ بـ DataFrame جديد فقط بالسجلات الجديدة
                    df = pd.DataFrame(records, columns=expected_columns)
            else:
                # إذا كان الملف غير موجود أو فارغ، نبدأ بـ DataFrame جديد فقط بالسجلات الجديدة
                df = pd.DataFrame(records, columns=expected_columns)

            try:
                # حفظ DataFrame النهائي في الملف
                df.to_csv(abs_file, index=False, encoding='utf-8-sig', sep=';') # استخدم الفاصلة المنقوطة
                messagebox.showinfo("تم", "تم حفظ الغياب بنجاح.", parent=att_win)
            except Exception as e:
                messagebox.showerror("خطأ في الحفظ", f"فشل حفظ بيانات الغياب في الملف: {str(e)}", parent=att_win)
                return

            # إنشاء نافذة منبثقة لاختيار نوع الإرسال
            send_win = tk.Toplevel(att_win)
            send_win.title("إرسال التقارير")
            send_win.geometry("400x200")
            send_win.configure(bg="#2e2e2e")

            def send_absence_reports():
                # دالة لإنشاء رسالة لكل طالب
                def create_message(record):
                    lesson_data = self.lessons[self.lessons["الحصة"] == lesson].iloc[0]
                    if record["الحالة"] == "حاضر":
                        return f"ابنك/ابنتك {record['الاسم']} حاضر اليوم في {lesson} ({lesson_data['الوقت']}) بتاريخ {date}.\n\n{{-تسجيل حضور أو غياب او تقارير الطالب عند أستاذ علي أبو بكر }}"
                    else:
                        return f"ابنك/ابنتك {record['الاسم']} غائب اليوم في {lesson} ({lesson_data['الوقت']}) بتاريخ {date}.\n\n{{-تسجيل حضور أو غياب او تقارير الطالب عند أستاذ علي أبو بكر }}"
                
                # فلترة السجلات التي لديها أرقام هواتف صالحة
                valid_records = [record for record in records 
                               if record["الهاتف"] and str(record["الهاتف"]).strip() != "nan"]
                
                if not valid_records:
                    messagebox.showwarning("تنبيه", "لا توجد أرقام هواتف صالحة للإرسال إليها.", parent=send_win)
                    send_win.destroy()
                    return
                
                # عرض رسالة تأكيد مع عدد الرسائل والوقت المتوقع
                total_messages = len(valid_records)
                estimated_batches = (total_messages + 59) // 60  # تقريب لأعلى
                estimated_time = estimated_batches  # دقيقة لكل دفعة (تقريباً)
                
                confirm_msg = f"سيتم إرسال {total_messages} رسالة على {estimated_batches} دفعة.\n"
                confirm_msg += f"الوقت المتوقع: حوالي {estimated_time} دقيقة.\n\n"
                confirm_msg += "هل تريد المتابعة؟"
                
                if not messagebox.askyesno("تأكيد الإرسال", confirm_msg, parent=send_win):
                    send_win.destroy()
                    return
                
                try:
                    # استخدام دالة الإرسال بالدفعات
                    success_count, failed_count, failed_msgs = send_whatsapp_batch(
                        valid_records, 
                        create_message,
                        batch_size=60,
                        delay_minutes=1
                    )
                    
                    if failed_count == 0:
                        messagebox.showinfo("تم", f"تم إرسال {success_count} تقرير غياب بنجاح.", parent=send_win)
                    else:
                        # إنشاء نافذة منبثقة لعرض الأخطاء مع زر إعادة المحاولة
                        error_win = tk.Toplevel(send_win)
                        error_win.title("نتيجة الإرسال")
                        error_win.geometry("600x400")
                        error_win.configure(bg="#2e2e2e")
                        
                        # إطار للرسالة الرئيسية
                        main_frame = tk.Frame(error_win, bg="#2e2e2e")
                        main_frame.pack(fill="x", padx=10, pady=10)
                        
                        result_text = f"تم إرسال {success_count} تقرير غياب بنجاح.\nفشل إرسال {failed_count} تقرير."
                        tk.Label(main_frame, text=result_text, bg="#2e2e2e", fg="white", 
                               font=("Helvetica", 12, "bold")).pack(pady=10)
                        
                        # إطار لقائمة الطلاب الفاشلين
                        list_frame = tk.Frame(error_win, bg="#2e2e2e")
                        list_frame.pack(fill="both", expand=True, padx=10, pady=5)
                        
                        tk.Label(list_frame, text="الطلاب الذين فشل إرسال التقارير إليهم:", 
                               bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
                        
                        # إنشاء قائمة للطلاب الفاشلين
                        failed_listbox = tk.Listbox(list_frame, font=("Helvetica", 11), height=10)
                        failed_listbox.pack(fill="both", expand=True)
                        
                        # إضافة شريط التمرير
                        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=failed_listbox.yview)
                        scrollbar.pack(side="right", fill="y")
                        failed_listbox.configure(yscrollcommand=scrollbar.set)
                        
                        # استخراج أسماء الطلاب الفاشلين من رسائل الأخطاء
                        failed_student_names = []
                        for msg in failed_msgs:
                            # استخراج اسم الطالب من رسالة الخطأ
                            if ":" in msg:
                                student_name = msg.split(":")[0].strip()
                                failed_student_names.append(student_name)
                                failed_listbox.insert(tk.END, student_name)
                        
                        # إطار للأزرار
                        btn_frame = tk.Frame(error_win, bg="#2e2e2e")
                        btn_frame.pack(fill="x", padx=10, pady=10)
                        
                        def retry_failed_students():
                            """إعادة المحاولة للطلاب الفاشلين فقط"""
                            if not failed_student_names:
                                messagebox.showwarning("تنبيه", "لا يوجد طلاب لإعادة المحاولة.", parent=error_win)
                                return
                            
                            # فلترة السجلات للطلاب الفاشلين فقط
                            retry_records = [record for record in valid_records 
                                           if record["الاسم"] in failed_student_names]
                            
                            if not retry_records:
                                messagebox.showwarning("تنبيه", "لا توجد بيانات صالحة للطلاب الفاشلين.", parent=error_win)
                                return
                            
                            # عرض رسالة تأكيد
                            retry_msg = f"سيتم إعادة المحاولة لـ {len(retry_records)} طالب.\nهل تريد المتابعة؟"
                            if not messagebox.askyesno("تأكيد إعادة المحاولة", retry_msg, parent=error_win):
                                return
                            
                            try:
                                # إعادة المحاولة
                                retry_success, retry_failed, retry_failed_msgs = send_whatsapp_batch(
                                    retry_records,
                                    create_message,
                                    batch_size=30,  # دفعة أصغر لإعادة المحاولة
                                    delay_minutes=2,  # انتظار أطول
                                    attachments=attachments_list if attachments_list else None
                                )
                                
                                if retry_failed == 0:
                                    messagebox.showinfo("تم", f"تم إرسال جميع التقارير بنجاح بعد إعادة المحاولة.", parent=error_win)
                                    error_win.destroy()
                                else:
                                    messagebox.showwarning("تنبيه", 
                                        f"تم إرسال {retry_success} تقرير بنجاح.\nفشل إرسال {retry_failed} تقرير بعد إعادة المحاولة.", 
                                        parent=error_win)
                                    
                            except Exception as e:
                                messagebox.showerror("خطأ", f"حدث خطأ أثناء إعادة المحاولة: {str(e)}", parent=error_win)
                            
                        # أزرار التحكم
                        retry_btn = tk.Button(btn_frame, text="إعادة المحاولة للطلاب الفاشلين", 
                                            command=retry_failed_students, bg="#ffaa00", fg="black", 
                                            font=("Helvetica", 12))
                        retry_btn.pack(side="left", padx=5)
                        
                        close_btn = tk.Button(btn_frame, text="إغلاق", command=error_win.destroy,
                                           bg="#cc3333", fg="white", font=("Helvetica", 12))
                        close_btn.pack(side="right", padx=5)
                        
                        # جعل النافذة في المنتصف
                        error_win.transient(send_win)
                        error_win.grab_set()
                        
                except Exception as e:
                    messagebox.showerror("خطأ", f"حدث خطأ أثناء الإرسال: {str(e)}", parent=send_win)
                
                send_win.destroy()

            # أزرار الإرسال
            btn_frame = tk.Frame(send_win, bg="#2e2e2e")
            btn_frame.pack(pady=20)

            tk.Button(btn_frame, text="إرسال تقارير الغياب", command=send_absence_reports,
                     bg="#00cc66", fg="white", font=("Helvetica", 12)).pack(side="left", padx=10)

            # جعل النافذة في المنتصف
            send_win.transient(att_win)
            send_win.grab_set()
            att_win.wait_window(send_win)

        # إضافة زر حفظ الغياب
        tk.Button(att_win, text="حفظ الغياب", font=("Helvetica", 12), bg="#00cc66", fg="white", command=save_attendance).pack(pady=10)

    def save_lessons(self):
        """حفظ بيانات الحصص في الملف"""
        try:
            self.lessons.to_csv(self.lessons_file, index=False, encoding='utf-8-sig', sep=';')
        except Exception as e:
            messagebox.showerror("خطأ", f"حدث خطأ أثناء حفظ بيانات الحصص: {str(e)}")

    def manage_lessons(self):
        win = tk.Toplevel(self.root)
        win.title("إدارة الحصص")
        win.geometry("600x500")
        win.configure(bg="#2e2e2e")

        # إطار للجدول
        table_frame = tk.Frame(win, bg="#2e2e2e")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # إنشاء جدول لعرض الحصص
        columns = ("lesson_name", "lesson_time", "lesson_desc")
        lessons_tree = ttk.Treeview(table_frame, columns=columns, show="headings", selectmode="browse")
        lessons_tree.heading("lesson_name", text="اسم الحصة")
        lessons_tree.heading("lesson_time", text="الوقت")
        lessons_tree.heading("lesson_desc", text="الوصف")

        # تحديد عرض الأعمدة
        lessons_tree.column("lesson_name", width=150, anchor="center")
        lessons_tree.column("lesson_time", width=100, anchor="center")
        lessons_tree.column("lesson_desc", width=200, anchor="center")

        # إضافة شريط تمرير
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=lessons_tree.yview)
        scrollbar.pack(side="right", fill="y")
        lessons_tree.configure(yscrollcommand=scrollbar.set)
        lessons_tree.pack(fill="both", expand=True)

        def load_lessons_to_tree():
            # مسح الجدول الحالي
            for item in lessons_tree.get_children():
                lessons_tree.delete(item)
            # إضافة الحصص من DataFrame
            for index, row in self.lessons.iterrows():
                lessons_tree.insert("", tk.END, values=(row["الحصة"], row["الوقت"], row["الوصف"]))

        # تحميل الحصص عند فتح النافذة
        load_lessons_to_tree()

        # إطار للأزرار
        btn_frame = tk.Frame(win, bg="#2e2e2e")
        btn_frame.pack(pady=10)

        def add_lesson():
            add_win = tk.Toplevel(win)
            add_win.title("إضافة حصة جديدة")
            add_win.geometry("400x300")
            add_win.configure(bg="#2e2e2e")

            tk.Label(add_win, text="اسم الحصة:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            name_entry = tk.Entry(add_win, font=("Helvetica", 12))
            add_copy_paste_support(name_entry)
            name_entry.pack(pady=5)

            tk.Label(add_win, text="الوقت:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            time_entry = tk.Entry(add_win, font=("Helvetica", 12))
            add_copy_paste_support(time_entry)
            time_entry.pack(pady=5)

            tk.Label(add_win, text="الوصف:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            desc_entry = tk.Entry(add_win, font=("Helvetica", 12))
            add_copy_paste_support(desc_entry)
            desc_entry.pack(pady=5)

            def save():
                name = name_entry.get().strip()
                time = time_entry.get().strip()
                desc = desc_entry.get().strip()

                if not (name and time):
                    messagebox.showwarning("تنبيه", "يرجى ملء اسم الحصة والوقت.", parent=add_win)
                    return

                # تم إزالة التحقق من تكرار اسم الحصة للسماح بإضافة حصص بنفس الاسم

                new_row = pd.DataFrame({"الحصة": [name], "الوقت": [time], "الوصف": [desc]})
                self.lessons = pd.concat([self.lessons, new_row], ignore_index=True)
                self.save_lessons()
                load_lessons_to_tree() # تحديث الجدول
                # تحديث قائمة الحصص في الكومبوبوكس في نافذة الغياب لو مفتوحة
                self.update_attendance_lesson_combo()
                add_win.destroy()
                messagebox.showinfo("تم", "تمت إضافة الحصة بنجاح.", parent=win)

            tk.Button(add_win, text="حفظ", command=save, bg="#00cc66", fg="white", font=("Helvetica", 12)).pack(pady=10)

        def edit_lesson():
            selected_item = lessons_tree.selection()
            if not selected_item:
                messagebox.showwarning("تنبيه", "يرجى اختيار حصة لتعديلها.", parent=win)
                return
            
            item_values = lessons_tree.item(selected_item)['values']
            old_name = item_values[0]

            edit_win = tk.Toplevel(win)
            edit_win.title(f"تعديل الحصة: {old_name}")
            edit_win.geometry("400x300")
            edit_win.configure(bg="#2e2e2e")

            tk.Label(edit_win, text="اسم الحصة:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            name_entry = tk.Entry(edit_win, font=("Helvetica", 12))
            add_copy_paste_support(name_entry)
            name_entry.insert(0, item_values[0])
            name_entry.pack(pady=5)

            tk.Label(edit_win, text="الوقت:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            time_entry = tk.Entry(edit_win, font=("Helvetica", 12))
            add_copy_paste_support(time_entry)
            time_entry.insert(0, item_values[1])
            time_entry.pack(pady=5)

            tk.Label(edit_win, text="الوصف:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            desc_entry = tk.Entry(edit_win, font=("Helvetica", 12))
            add_copy_paste_support(desc_entry)
            desc_entry.insert(0, item_values[2])
            desc_entry.pack(pady=5)

            def save_changes():
                new_name = name_entry.get().strip()
                new_time = time_entry.get().strip()
                new_desc = desc_entry.get().strip()

                if not (new_name and new_time):
                    messagebox.showwarning("تنبيه", "يرجى ملء اسم الحصة والوقت.", parent=edit_win)
                    return

                # تم إزالة التحقق من تكرار اسم الحصة للسماح بإضافة حصص بنفس الاسم

                # العثور على الصف في DataFrame بناءً على الاسم القديم وتحديثه
                lesson_index = self.lessons[self.lessons["الحصة"] == old_name].index[0]
                self.lessons.loc[lesson_index, "الحصة"] = new_name
                self.lessons.loc[lesson_index, "الوقت"] = new_time
                self.lessons.loc[lesson_index, "الوصف"] = new_desc
                
                self.save_lessons()
                load_lessons_to_tree() # تحديث الجدول
                 # تحديث قائمة الحصص في الكومبوبوكس في نافذة الغياب لو مفتوحة
                self.update_attendance_lesson_combo()
                edit_win.destroy()
                messagebox.showinfo("تم", "تم تعديل الحصة بنجاح.", parent=win)

            tk.Button(edit_win, text="حفظ التغييرات", command=save_changes, bg="#00cc66", fg="white", font=("Helvetica", 12)).pack(pady=10)

        def delete_lesson():
            selected_item = lessons_tree.selection()
            if not selected_item:
                messagebox.showwarning("تنبيه", "يرجى اختيار حصة لحذفها.", parent=win)
                return

            item_values = lessons_tree.item(selected_item)['values']
            lesson_name = item_values[0]

            confirm = messagebox.askyesno("تأكيد الحذف", f"هل أنت متأكد أنك تريد حذف الحصة '{lesson_name}'؟", parent=win)
            if confirm:
                # حذف الصف من DataFrame بناءً على اسم الحصة
                self.lessons = self.lessons[self.lessons["الحصة"] != lesson_name]
                self.save_lessons()
                load_lessons_to_tree() # تحديث الجدول
                 # تحديث قائمة الحصص في الكومبوبوكس في نافذة الغياب لو مفتوحة
                self.update_attendance_lesson_combo()
                messagebox.showinfo("تم", "تم حذف الحصة بنجاح.", parent=win)

        # أزرار إدارة الحصص
        add_btn = tk.Button(btn_frame, text="إضافة حصة", command=add_lesson, bg="#00cc66", fg="white", font=("Helvetica", 12))
        add_btn.pack(side="left", padx=5)

        edit_btn = tk.Button(btn_frame, text="تعديل حصة", command=edit_lesson, bg="#ffaa00", fg="black", font=("Helvetica", 12))
        edit_btn.pack(side="left", padx=5)

        delete_btn = tk.Button(btn_frame, text="حذف حصة", command=delete_lesson, bg="#cc3333", fg="white", font=("Helvetica", 12))
        delete_btn.pack(side="left", padx=5)

    # إضافة دالة لتحديث الكومبوبوكس في نافذة الغياب
    def update_attendance_lesson_combo(self):
        # البحث عن نوافذ تسجيل الغياب المفتوحة وتحديث الكومبوبوكس الخاص بها
        # هذه طريقة مبسطة وقد تحتاج لتحسين إذا كان هناك أكثر من نافذة غياب مفتوحة
        # أو إذا كانت النوافذ ليست Toplevels مباشرة من root
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Toplevel) and widget.title().startswith("تسجيل الغياب"):
                # البحث عن الكومبوبوكس داخل النافذة
                # هذه طريقة هشة وتعتمد على هيكل الواجهة الداخلي
                # قد تحتاج لتمرير الكومبوبوكس عند فتح النافذة لتحسين الموثوقية
                for child in widget.winfo_walk():
                    if isinstance(child, ttk.Combobox):
                         # التحقق مما إذا كان هذا الكومبوبوكس هو الخاص بالحصة
                         # يمكن إضافة اسم خاص للكومبوبوكس للتحقق منه بدقة
                         # حاليا نفترض أنه الكومبوبوكس الأول (والوحيد عادة) لنص الحصة
                         combo = child
                         # إنشاء قائمة الحصص مع الوقت للتمييز بين الحصص المتشابهة
                         lesson_values = []
                         for _, row in self.lessons.iterrows():
                             lesson_name = row["الحصة"]
                             lesson_time = row["الوقت"]
                             lesson_values.append(f"{lesson_name} - {lesson_time}")
                         
                         combo['values'] = lesson_values
                         # ممكن نحتفظ بالقيمة المختارة لو كانت موجودة في القائمة الجديدة
                         current_lesson = combo.get()
                         if current_lesson and current_lesson not in lesson_values:
                              combo.set('') # مسح الاختيار لو الحصة المحذوفة كانت مختارة
                         break # توقف بعد العثور على الكومبوبوكس الأول المناسب

    def import_students_from_csv(self):
        file_path = fd.askopenfilename(
            title="اختر ملف CSV",
            filetypes=[("CSV files", "*.csv")]
        )
        if not file_path:
            return
        try:
            df = pd.read_csv(file_path, encoding='utf-8-sig', sep=';', dtype={"الهاتف": str})
            expected_cols = ["الاسم", "الصف", "البريد", "المجموعة", "الهاتف"]
            # إذا الأعمدة غير مطابقة، حاول تعيينها تلقائيًا بناءً على أول 5 أعمدة
            if not all(col in df.columns for col in expected_cols):
                df = df.iloc[:, :5]
                df.columns = expected_cols
            df.to_csv(STUDENT_FILE, index=False, encoding='utf-8-sig', sep=';')
            self.students = df
            messagebox.showinfo("تم", "تم استيراد الطلاب من CSV بنجاح!")
        except Exception as e:
            messagebox.showerror("خطأ", f"فشل استيراد البيانات: {str(e)}")

    def import_groups_from_csv(self):
        file_path = fd.askopenfilename(
            title="اختر ملف CSV للمجموعات",
            filetypes=[("CSV files", "*.csv")]
        )
        if not file_path:
            return
        try:
            df = pd.read_csv(file_path, encoding='utf-8-sig', sep=';')
            expected_cols = ["المجموعة", "الصف"]
            # إذا الأعمدة غير مطابقة، حاول تعيينها تلقائيًا بناءً على أول عمودين
            if not all(col in df.columns for col in expected_cols):
                df = df.iloc[:, :2]
                df.columns = expected_cols
            df.to_csv(GROUP_FILE, index=False, encoding='utf-8-sig', sep=';')
            self.groups = df
            # تحديث قائمة المجموعات في الكومبوبوكس
            self.group_combo['values'] = self.groups["المجموعة"].tolist()
            messagebox.showinfo("تم", "تم استيراد المجموعات من CSV بنجاح!")
        except Exception as e:
            messagebox.showerror("خطأ", f"فشل استيراد بيانات المجموعات: {str(e)}")

    def manage_exams(self):
        """إدارة الامتحانات والدرجات"""
        win = tk.Toplevel(self.root)
        win.title("إدارة الامتحانات والدرجات")
        win.geometry("1000x700")
        win.configure(bg="#2e2e2e")
        
        # تحميل بيانات الامتحانات
        self.load_exams()
        
        # إطار العنوان
        title_frame = tk.Frame(win, bg="#2e2e2e")
        title_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(title_frame, text="إدارة الامتحانات والدرجات", 
                bg="#2e2e2e", fg="white", font=("SegoeUI", 16, "bold")).pack()
        
        # إطار الأزرار
        btn_frame = tk.Frame(win, bg="#2e2e2e")
        btn_frame.pack(fill="x", padx=10, pady=5)
        
        def create_exam():
            """إنشاء امتحان جديد"""
            exam_win = tk.Toplevel(win)
            exam_win.title("إنشاء امتحان جديد")
            exam_win.geometry("500x400")
            exam_win.configure(bg="#2e2e2e")
            
            tk.Label(exam_win, text="اسم الامتحان:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            exam_name_entry = tk.Entry(exam_win, font=("Helvetica", 12))
            add_copy_paste_support(exam_name_entry)
            exam_name_entry.pack(pady=5)
            
            tk.Label(exam_win, text="الدرجة الكلية:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            total_grade_entry = tk.Entry(exam_win, font=("Helvetica", 12))
            add_copy_paste_support(total_grade_entry)
            total_grade_entry.pack(pady=5)
            
            tk.Label(exam_win, text="التاريخ:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            date_var = tk.StringVar()
            def pick_date():
                import tkcalendar
                cal_win = tk.Toplevel(exam_win)
                cal_win.title("اختر التاريخ")
                cal = tkcalendar.Calendar(cal_win, selectmode='day', date_pattern='yyyy-mm-dd')
                cal.pack(padx=10, pady=10)
                def set_date():
                    date_var.set(cal.get_date())
                    cal_win.destroy()
                tk.Button(cal_win, text="اختيار", command=set_date).pack(pady=5)
            date_entry = tk.Entry(exam_win, textvariable=date_var, font=("Helvetica", 12), state="readonly")
            date_entry.pack(pady=5)
            tk.Button(exam_win, text="...", command=pick_date, font=("Helvetica", 10)).pack(pady=5)
            
            tk.Label(exam_win, text="الصف:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            grade_var = tk.StringVar()
            grade_combo = ttk.Combobox(exam_win, textvariable=grade_var,
                                      values=["الصف الأول الثانوي", "الصف الثاني الثانوي", "الصف الثالث الثانوي"],
                                      state="readonly", font=("Helvetica", 12))
            grade_combo.pack(pady=5)
            
            tk.Label(exam_win, text="الوصف (اختياري):", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
            desc_entry = tk.Entry(exam_win, font=("Helvetica", 12))
            add_copy_paste_support(desc_entry)
            desc_entry.pack(pady=5)
            
            def save_exam():
                name = exam_name_entry.get().strip()
                total_grade = total_grade_entry.get().strip()
                date = date_var.get()
                selected_grade = grade_var.get()
                desc = desc_entry.get().strip()
                
                if not (name and total_grade and date and selected_grade):
                    messagebox.showwarning("تنبيه", "يرجى ملء اسم الامتحان والدرجة الكلية والتاريخ والصف.", parent=exam_win)
                    return
                
                try:
                    total_grade = float(total_grade)
                    if total_grade <= 0:
                        messagebox.showwarning("تنبيه", "الدرجة الكلية يجب أن تكون أكبر من صفر.", parent=exam_win)
                        return
                except ValueError:
                    messagebox.showwarning("تنبيه", "الدرجة الكلية يجب أن تكون رقم.", parent=exam_win)
                    return
                
                # إنشاء امتحان جديد
                new_exam = pd.DataFrame({
                    "اسم_الامتحان": [name],
                    "الدرجة_الكلية": [total_grade],
                    "التاريخ": [date],
                    "الوصف": [desc],
                    "الصف": [selected_grade],
                    "الحالة": ["مفتوح"]
                })
                
                if hasattr(self, 'exams') and not self.exams.empty:
                    self.exams = pd.concat([self.exams, new_exam], ignore_index=True)
                else:
                    self.exams = new_exam
                
                self.save_exams()
                load_exams_to_tree()
                exam_win.destroy()
                messagebox.showinfo("تم", "تم إنشاء الامتحان بنجاح.", parent=win)
            
            tk.Button(exam_win, text="إنشاء الامتحان", command=save_exam, bg="#00cc66", fg="white", 
                     font=("Helvetica", 12)).pack(pady=20)
        
        def enter_grades():
            """إدخال درجات الطلاب"""
            selected_item = exams_tree.selection()
            if not selected_item:
                messagebox.showwarning("تنبيه", "يرجى اختيار امتحان لإدخال الدرجات.", parent=win)
                return
            
            item_values = exams_tree.item(selected_item)['values']
            exam_name = item_values[0]
            total_grade = float(item_values[1])
            exam_grade = item_values[5]  # الصف
            
            # فتح نافذة إدخال الدرجات
            grades_win = tk.Toplevel(win)
            grades_win.title(f"إدخال درجات - {exam_name}")
            grades_win.geometry("900x700")
            grades_win.configure(bg="#2e2e2e")
            
            # تحميل درجات الامتحان إذا وجدت
            self.load_exam_grades()
            exam_grades = self.get_exam_grades(exam_name)
            
            # إطار العنوان
            title_frame = tk.Frame(grades_win, bg="#2e2e2e")
            title_frame.pack(fill="x", padx=10, pady=10)
            
            tk.Label(title_frame, text=f"إدخال درجات امتحان: {exam_name}", 
                    bg="#2e2e2e", fg="white", font=("SegoeUI", 14, "bold")).pack()
            tk.Label(title_frame, text=f"الدرجة الكلية: {total_grade}", 
                    bg="#2e2e2e", fg="yellow", font=("SegoeUI", 12)).pack()
            
            # إطار اختيار المجموعة
            group_frame = tk.Frame(grades_win, bg="#2e2e2e")
            group_frame.pack(fill="x", padx=10, pady=5)
            
            tk.Label(group_frame, text="اختر المجموعة:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
            group_var = tk.StringVar()
            
            # الحصول على المجموعات المتاحة للصف المحدد
            available_groups = []
            grade_students = self.students[self.students["الصف"] == exam_grade]
            for _, student in grade_students.iterrows():
                group = student.get("المجموعة", "")
                if group and group not in available_groups and str(group).strip() != "nan":
                    available_groups.append(group)
            
            group_combo = ttk.Combobox(group_frame, textvariable=group_var,
                                      values=["جميع الطلاب"] + available_groups,
                                      state="readonly", font=("SegoeUI", 12))
            group_combo.pack(side="left", padx=5)
            group_combo.set("جميع الطلاب")  # القيمة الافتراضية
            
            def load_students_to_tree():
                """تحميل الطلاب في الجدول"""
                for item in grades_tree.get_children():
                    grades_tree.delete(item)
                
                # تصفية الطلاب حسب الصف المحدد في الامتحان
                grade_students = self.students[self.students["الصف"] == exam_grade]
                
                # تصفية إضافية حسب المجموعة المختارة
                selected_group = group_var.get()
                if selected_group and selected_group != "جميع الطلاب":
                    grade_students = grade_students[grade_students["المجموعة"] == selected_group]
                
                for _, student in grade_students.iterrows():
                    student_name = student["الاسم"]
                    student_group = student.get("المجموعة", "")
                    current_grade = exam_grades.get(student_name, "")
                    percentage = ""
                    if current_grade:
                        try:
                            grade_val = float(current_grade)
                            percentage = f"{(grade_val/total_grade)*100:.1f}%"
                        except:
                            pass
                    
                    grades_tree.insert("", "end", values=(student_name, student_group, current_grade, percentage))
            
            def filter_students():
                """تصفية الطلاب حسب البحث"""
                search_text = search_var.get().strip().lower()
                for item in grades_tree.get_children():
                    grades_tree.delete(item)
                
                # تصفية الطلاب حسب الصف المحدد في الامتحان
                grade_students = self.students[self.students["الصف"] == exam_grade]
                
                # تصفية إضافية حسب المجموعة المختارة
                selected_group = group_var.get()
                if selected_group and selected_group != "جميع الطلاب":
                    grade_students = grade_students[grade_students["المجموعة"] == selected_group]
                
                # تصفية حسب نص البحث
                if search_text:
                    filtered_students = grade_students[
                        grade_students["الاسم"].str.lower().str.contains(search_text, na=False)
                    ]
                else:
                    filtered_students = grade_students
                
                for _, student in filtered_students.iterrows():
                    student_name = student["الاسم"]
                    student_group = student.get("المجموعة", "")
                    current_grade = exam_grades.get(student_name, "")
                    percentage = ""
                    if current_grade:
                        try:
                            grade_val = float(current_grade)
                            percentage = f"{(grade_val/total_grade)*100:.1f}%"
                        except:
                            pass
                    
                    grades_tree.insert("", "end", values=(student_name, student_group, current_grade, percentage))
            
            def update_stats():
                """تحديث الإحصائيات"""
                # مسح الإحصائيات السابقة
                for widget in stats_frame.winfo_children():
                    widget.destroy()
                
                # جمع الدرجات المدخلة
                grades_list = []
                top_students = []
                
                for item in grades_tree.get_children():
                    values = grades_tree.item(item)['values']
                    student_name = values[0]
                    grade = values[2]
                    
                    if grade and grade != "":
                        try:
                            grade_val = float(grade)
                            grades_list.append(grade_val)
                            top_students.append((student_name, grade_val))
                        except:
                            pass
                
                if grades_list:
                    # الإحصائيات الأساسية
                    basic_stats_frame = tk.Frame(stats_frame, bg="#2e2e2e")
                    basic_stats_frame.pack(fill="x", pady=2)
                    
                    avg_grade = sum(grades_list) / len(grades_list)
                    max_grade = max(grades_list)
                    min_grade = min(grades_list)
                    passed_count = len([g for g in grades_list if g >= total_grade * 0.5])
                    total_students = len(grades_list)
                    
                    tk.Label(basic_stats_frame, text=f"📊 متوسط الدرجات: {avg_grade:.2f}", 
                            bg="#2e2e2e", fg="cyan", font=("Helvetica", 10)).pack(side="left", padx=5)
                    tk.Label(basic_stats_frame, text=f"🎯 أعلى درجة: {max_grade}", 
                            bg="#2e2e2e", fg="green", font=("Helvetica", 10)).pack(side="left", padx=5)
                    tk.Label(basic_stats_frame, text=f"📉 أقل درجة: {min_grade}", 
                            bg="#2e2e2e", fg="red", font=("Helvetica", 10)).pack(side="left", padx=5)
                    tk.Label(basic_stats_frame, text=f"✅ الناجحون: {passed_count}/{total_students}", 
                            bg="#2e2e2e", fg="yellow", font=("Helvetica", 10)).pack(side="left", padx=5)
                    
                    # أفضل الطلاب
                    if top_students:
                        top_students.sort(key=lambda x: x[1], reverse=True)
                        top_frame = tk.Frame(stats_frame, bg="#2e2e2e")
                        top_frame.pack(fill="x", pady=2)
                        
                        tk.Label(top_frame, text="🏆 أفضل الطلاب:", 
                                bg="#2e2e2e", fg="gold", font=("Helvetica", 10, "bold")).pack(side="left", padx=5)
                        
                        for i, (student_name, grade_val) in enumerate(top_students[:3]):
                            if i == 0:
                                medal = "🥇"
                                color = "gold"
                            elif i == 1:
                                medal = "🥈"
                                color = "silver"
                            else:
                                medal = "🥉"
                                color = "orange"
                            
                            percentage = f"{(grade_val/total_grade)*100:.1f}%"
                            tk.Label(top_frame, text=f"{medal} {student_name}: {grade_val} ({percentage})", 
                                    bg="#2e2e2e", fg=color, font=("Helvetica", 9)).pack(side="left", padx=3)
            
            # تحديث الإحصائيات عند تحميل الطلاب
            def load_students_with_stats():
                load_students_to_tree()
                update_stats()
            
            # زر تحديث الجدول
            tk.Button(group_frame, text="تحديث الجدول", command=load_students_with_stats, 
                     bg="#0066cc", fg="white", font=("SegoeUI", 10)).pack(side="left", padx=10)
            
            # إطار البحث
            search_frame = tk.Frame(grades_win, bg="#2e2e2e")
            search_frame.pack(fill="x", padx=10, pady=5)
            
            tk.Label(search_frame, text="البحث عن طالب:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
            search_var = tk.StringVar()
            search_entry = create_arabic_entry_widget(search_frame, textvariable=search_var, font=("SegoeUI", 12))
            search_entry.pack(side="left", padx=5, fill="x", expand=True)
            
            # جدول الطلاب والدرجات
            table_frame = tk.Frame(grades_win, bg="#2e2e2e")
            table_frame.pack(fill="both", expand=True, padx=10, pady=10)
            
            columns = ("name", "group", "grade", "percentage")
            grades_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
            grades_tree.heading("name", text="اسم الطالب")
            grades_tree.heading("group", text="المجموعة")
            grades_tree.heading("grade", text="الدرجة")
            grades_tree.heading("percentage", text="النسبة المئوية")
            grades_tree.column("name", width=250)
            grades_tree.column("group", width=120)
            grades_tree.column("grade", width=120)
            grades_tree.column("percentage", width=120)
            grades_tree.pack(fill="both", expand=True)
            
            # شريط التمرير
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=grades_tree.yview)
            scrollbar.pack(side="right", fill="y")
            grades_tree.configure(yscrollcommand=scrollbar.set)
            
            # إطار الإحصائيات
            stats_frame = tk.Frame(grades_win, bg="#2e2e2e")
            stats_frame.pack(fill="x", padx=10, pady=5)
            
            # تحديث الإحصائيات عند تحميل الطلاب
            def load_students_with_stats():
                load_students_to_tree()
                update_stats()
            
            # تحديث الإحصائيات عند البحث
            def filter_students_with_stats():
                filter_students()
                update_stats()
            
            # ربط دالة البحث المحدثة
            search_entry.bind("<KeyRelease>", lambda e: filter_students_with_stats())
            
            def on_double_click(event):
                """تعديل الدرجة عند النقر المزدوج"""
                item = grades_tree.identify_row(event.y)
                if item:
                    current_values = grades_tree.item(item)['values']
                    student_name = current_values[0]
                    student_group = current_values[1]
                    
                    # نافذة إدخال الدرجة
                    grade_win = tk.Toplevel(grades_win)
                    grade_win.title(f"إدخال درجة {student_name}")
                    grade_win.geometry("350x250")
                    grade_win.configure(bg="#2e2e2e")
                    
                    tk.Label(grade_win, text=f"الطالب: {student_name}", 
                            bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=10)
                    tk.Label(grade_win, text=f"المجموعة: {student_group}", 
                            bg="#2e2e2e", fg="cyan", font=("Helvetica", 12)).pack(pady=5)
                    tk.Label(grade_win, text=f"الدرجة الكلية: {total_grade}", 
                            bg="#2e2e2e", fg="yellow", font=("Helvetica", 12)).pack(pady=5)
                    
                    tk.Label(grade_win, text="الدرجة:", bg="#2e2e2e", fg="white", font=("Helvetica", 12)).pack(pady=5)
                    grade_entry = tk.Entry(grade_win, font=("Helvetica", 12))
                    grade_entry.insert(0, current_values[2] if current_values[2] else "")
                    grade_entry.pack(pady=5)
                    
                    def save_grade():
                        grade = grade_entry.get().strip()
                        if grade:
                            try:
                                grade_val = float(grade)
                                if grade_val < 0 or grade_val > total_grade:
                                    messagebox.showwarning("تنبيه", f"الدرجة يجب أن تكون بين 0 و {total_grade}", parent=grade_win)
                                    return
                            except ValueError:
                                messagebox.showwarning("تنبيه", "الدرجة يجب أن تكون رقم.", parent=grade_win)
                                return
                        else:
                            grade_val = ""
                        
                        # حفظ الدرجة
                        self.save_student_grade(exam_name, student_name, grade_val)
                        
                        # إرسال تقرير تلقائي إذا كانت الدرجة موجودة
                        if grade_val:
                            self.send_exam_report(student_name, exam_name, grade_val, total_grade)
                        
                        # تحديث الجدول والإحصائيات
                        load_students_with_stats()
                        grade_win.destroy()
                    
                    tk.Button(grade_win, text="حفظ", command=save_grade, bg="#00cc66", fg="white", 
                             font=("Helvetica", 12)).pack(pady=10)
            
            # ربط دالة البحث المحدثة
            search_entry.bind("<KeyRelease>", lambda e: filter_students_with_stats())
            
            grades_tree.bind("<Double-1>", on_double_click)
            load_students_with_stats()
        
        def view_results():
            """عرض نتائج الامتحان"""
            selected_item = exams_tree.selection()
            if not selected_item:
                messagebox.showwarning("تنبيه", "يرجى اختيار امتحان لعرض النتائج.", parent=win)
                return
            
            item_values = exams_tree.item(selected_item)['values']
            exam_name = item_values[0]
            total_grade = float(item_values[1])
            exam_grade = item_values[5]  # الصف
            
            # تحميل درجات الامتحان
            self.load_exam_grades()
            exam_grades = self.get_exam_grades(exam_name)
            
            # نافذة عرض النتائج
            results_win = tk.Toplevel(win)
            results_win.title(f"نتائج امتحان - {exam_name}")
            results_win.geometry("800x600")
            results_win.configure(bg="#2e2e2e")
            
            # إطار العنوان
            title_frame = tk.Frame(results_win, bg="#2e2e2e")
            title_frame.pack(fill="x", padx=10, pady=10)
            
            tk.Label(title_frame, text=f"نتائج امتحان: {exam_name}", 
                    bg="#2e2e2e", fg="white", font=("SegoeUI", 14, "bold")).pack()
            
            # إطار اختيار المجموعة
            group_frame = tk.Frame(results_win, bg="#2e2e2e")
            group_frame.pack(fill="x", padx=10, pady=5)
            
            tk.Label(group_frame, text="اختر المجموعة:", bg="#2e2e2e", fg="white", font=("SegoeUI", 12)).pack(side="left", padx=5)
            group_var = tk.StringVar()
            
            # الحصول على المجموعات المتاحة للصف المحدد
            available_groups = []
            grade_students = self.students[self.students["الصف"] == exam_grade]
            for _, student in grade_students.iterrows():
                group = student.get("المجموعة", "")
                if group and group not in available_groups and str(group).strip() != "nan":
                    available_groups.append(group)
            
            group_combo = ttk.Combobox(group_frame, textvariable=group_var,
                                      values=["جميع الطلاب"] + available_groups,
                                      state="readonly", font=("SegoeUI", 12))
            group_combo.pack(side="left", padx=5)
            group_combo.set("جميع الطلاب")  # القيمة الافتراضية
            
            def load_results_to_tree():
                """تحميل النتائج في الجدول"""
                for item in results_tree.get_children():
                    results_tree.delete(item)
                
                # تصفية الطلاب حسب الصف المحدد في الامتحان
                grade_students = self.students[self.students["الصف"] == exam_grade]
                
                # تصفية إضافية حسب المجموعة المختارة
                selected_group = group_var.get()
                if selected_group and selected_group != "جميع الطلاب":
                    grade_students = grade_students[grade_students["المجموعة"] == selected_group]
                
                grades_list = []
                for _, student in grade_students.iterrows():
                    student_name = student["الاسم"]
                    grade = exam_grades.get(student_name, "")
                    percentage = ""
                    status = "غير محدد"
                    
                    if grade and grade != "":
                        try:
                            grade_val = float(grade)
                            percentage = f"{(grade_val/total_grade)*100:.1f}%"
                            if grade_val >= total_grade * 0.5:
                                status = "ناجح"
                            else:
                                status = "راسب"
                            grades_list.append(grade_val)
                        except:
                            pass
                    
                    results_tree.insert("", "end", values=(student_name, grade, percentage, status))
                
                # تحديث الإحصائيات
                if grades_list:
                    avg_grade = sum(grades_list) / len(grades_list)
                    max_grade = max(grades_list)
                    min_grade = min(grades_list)
                    passed_count = len([g for g in grades_list if g >= total_grade * 0.5])
                    total_students = len(grades_list)
                    
                    # العثور على أفضل الطلاب
                    top_students = []
                    for _, student in grade_students.iterrows():
                        student_name = student["الاسم"]
                        grade = exam_grades.get(student_name, "")
                        if grade and grade != "":
                            try:
                                grade_val = float(grade)
                                top_students.append((student_name, grade_val))
                            except:
                                pass
                    
                    # ترتيب الطلاب حسب الدرجات (تنازلي)
                    top_students.sort(key=lambda x: x[1], reverse=True)
                    
                    # تحديث الإحصائيات في الإطار
                    for widget in stats_frame.winfo_children():
                        widget.destroy()
                    
                    # الإحصائيات الأساسية
                    basic_stats_frame = tk.Frame(stats_frame, bg="#2e2e2e")
                    basic_stats_frame.pack(fill="x", pady=5)
                    
                    tk.Label(basic_stats_frame, text=f"متوسط الدرجات: {avg_grade:.2f}", 
                            bg="#2e2e2e", fg="cyan", font=("Helvetica", 12)).pack(side="left", padx=10)
                    tk.Label(basic_stats_frame, text=f"أعلى درجة: {max_grade}", 
                            bg="#2e2e2e", fg="green", font=("Helvetica", 12)).pack(side="left", padx=10)
                    tk.Label(basic_stats_frame, text=f"أقل درجة: {min_grade}", 
                            bg="#2e2e2e", fg="red", font=("Helvetica", 12)).pack(side="left", padx=10)
                    tk.Label(basic_stats_frame, text=f"عدد الناجحين: {passed_count}/{total_students}", 
                            bg="#2e2e2e", fg="yellow", font=("Helvetica", 12)).pack(side="left", padx=10)
                    
                    # إطار أفضل الطلاب
                    top_students_frame = tk.Frame(stats_frame, bg="#2e2e2e")
                    top_students_frame.pack(fill="x", pady=5)
                    
                    tk.Label(top_students_frame, text="🏆 أفضل الطلاب:", 
                            bg="#2e2e2e", fg="gold", font=("Helvetica", 12, "bold")).pack(side="left", padx=10)
                    
                    # عرض أفضل 3 طلاب
                    for i, (student_name, grade_val) in enumerate(top_students[:3]):
                        if i == 0:
                            medal = "🥇"
                            color = "gold"
                        elif i == 1:
                            medal = "🥈"
                            color = "silver"
                        else:
                            medal = "🥉"
                            color = "orange"
                        
                        percentage = f"{(grade_val/total_grade)*100:.1f}%"
                        tk.Label(top_students_frame, text=f"{medal} {student_name}: {grade_val} ({percentage})", 
                                bg="#2e2e2e", fg=color, font=("Helvetica", 11)).pack(side="left", padx=5)
                    
                    # إطار إحصائيات إضافية
                    extra_stats_frame = tk.Frame(stats_frame, bg="#2e2e2e")
                    extra_stats_frame.pack(fill="x", pady=5)
                    
                    # حساب النسبة المئوية للنجاح
                    success_rate = (passed_count / total_students) * 100 if total_students > 0 else 0
                    tk.Label(extra_stats_frame, text=f"نسبة النجاح: {success_rate:.1f}%", 
                            bg="#2e2e2e", fg="lime", font=("Helvetica", 11)).pack(side="left", padx=10)
                    
                    # حساب الانحراف المعياري
                    if len(grades_list) > 1:
                        variance = sum((x - avg_grade) ** 2 for x in grades_list) / len(grades_list)
                        std_dev = variance ** 0.5
                        tk.Label(extra_stats_frame, text=f"الانحراف المعياري: {std_dev:.2f}", 
                                bg="#2e2e2e", fg="lightblue", font=("Helvetica", 11)).pack(side="left", padx=10)
                    
                    # حساب النطاق
                    grade_range = max_grade - min_grade
                    tk.Label(extra_stats_frame, text=f"نطاق الدرجات: {grade_range:.1f}", 
                            bg="#2e2e2e", fg="pink", font=("Helvetica", 11)).pack(side="left", padx=10)
            
            # زر تحديث الجدول
            tk.Button(group_frame, text="تحديث الجدول", command=load_results_to_tree, 
                     bg="#0066cc", fg="white", font=("SegoeUI", 10)).pack(side="left", padx=10)
            
            # إحصائيات
            stats_frame = tk.Frame(results_win, bg="#2e2e2e")
            stats_frame.pack(fill="x", padx=10, pady=5)
            
            # جدول النتائج
            table_frame = tk.Frame(results_win, bg="#2e2e2e")
            table_frame.pack(fill="both", expand=True, padx=10, pady=10)
            
            columns = ("name", "grade", "percentage", "status")
            results_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
            results_tree.heading("name", text="اسم الطالب")
            results_tree.heading("grade", text="الدرجة")
            results_tree.heading("percentage", text="النسبة المئوية")
            results_tree.heading("status", text="الحالة")
            results_tree.column("name", width=250)
            results_tree.column("grade", width=100)
            results_tree.column("percentage", width=120)
            results_tree.column("status", width=100)
            results_tree.pack(fill="both", expand=True)
            
            # شريط التمرير
            scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=results_tree.yview)
            scrollbar.pack(side="right", fill="y")
            results_tree.configure(yscrollcommand=scrollbar.set)
            
            # تحميل النتائج الأولية
            load_results_to_tree()
        
        def delete_exam():
            """حذف امتحان"""
            selected_item = exams_tree.selection()
            if not selected_item:
                messagebox.showwarning("تنبيه", "يرجى اختيار امتحان لحذفه.", parent=win)
                return
            
            item_values = exams_tree.item(selected_item)['values']
            exam_name = item_values[0]
            
            confirm = messagebox.askyesno("تأكيد الحذف", f"هل أنت متأكد أنك تريد حذف الامتحان '{exam_name}'؟\nسيتم حذف جميع درجات الطلاب في هذا الامتحان.", parent=win)
            if confirm:
                # حذف الامتحان
                self.exams = self.exams[self.exams["اسم_الامتحان"] != exam_name]
                self.save_exams()
                
                # حذف درجات الامتحان
                self.delete_exam_grades(exam_name)
                
                load_exams_to_tree()
                messagebox.showinfo("تم", "تم حذف الامتحان بنجاح.", parent=win)
        
        # أزرار التحكم
        tk.Button(btn_frame, text="إنشاء امتحان جديد", command=create_exam, bg="#00cc66", fg="white", 
                 font=("Helvetica", 12)).pack(side="left", padx=5)
        tk.Button(btn_frame, text="إدخال درجات", command=enter_grades, bg="#ffaa00", fg="black", 
                 font=("Helvetica", 12)).pack(side="left", padx=5)
        tk.Button(btn_frame, text="عرض النتائج", command=view_results, bg="#0066cc", fg="white", 
                 font=("Helvetica", 12)).pack(side="left", padx=5)
        tk.Button(btn_frame, text="حذف امتحان", command=delete_exam, bg="#cc3333", fg="white", 
                 font=("Helvetica", 12)).pack(side="left", padx=5)
        
        # جدول الامتحانات
        table_frame = tk.Frame(win, bg="#2e2e2e")
        table_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        columns = ("name", "total_grade", "grade", "date", "description", "status")
        exams_tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=15)
        exams_tree.heading("name", text="اسم الامتحان")
        exams_tree.heading("total_grade", text="الدرجة الكلية")
        exams_tree.heading("grade", text="الصف")
        exams_tree.heading("date", text="التاريخ")
        exams_tree.heading("description", text="الوصف")
        exams_tree.heading("status", text="الحالة")
        exams_tree.column("name", width=180)
        exams_tree.column("total_grade", width=100)
        exams_tree.column("grade", width=120)
        exams_tree.column("date", width=100)
        exams_tree.column("description", width=180)
        exams_tree.column("status", width=80)
        exams_tree.pack(fill="both", expand=True)
        
        # شريط التمرير
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=exams_tree.yview)
        scrollbar.pack(side="right", fill="y")
        exams_tree.configure(yscrollcommand=scrollbar.set)
        
        def load_exams_to_tree():
            """تحميل الامتحانات في الجدول"""
            for item in exams_tree.get_children():
                exams_tree.delete(item)
            
            if hasattr(self, 'exams') and not self.exams.empty:
                for _, exam in self.exams.iterrows():
                    exams_tree.insert("", "end", values=(
                        exam["اسم_الامتحان"],
                        exam["الدرجة_الكلية"],
                        exam["التاريخ"],
                        exam["الوصف"],
                        exam["الحالة"],
                        exam["الصف"]
                    ))
        
        load_exams_to_tree()
    
    def load_exams(self):
        """تحميل بيانات الامتحانات"""
        try:
            if os.path.exists("exams.csv"):
                self.exams = pd.read_csv("exams.csv", encoding='utf-8-sig', sep=';')
            else:
                self.exams = pd.DataFrame(columns=["اسم_الامتحان", "الدرجة_الكلية", "التاريخ", "الوصف", "الصف", "الحالة"])
        except Exception as e:
            print(f"خطأ في تحميل الامتحانات: {e}")
            self.exams = pd.DataFrame(columns=["اسم_الامتحان", "الدرجة_الكلية", "التاريخ", "الوصف", "الصف", "الحالة"])
    
    def save_exams(self):
        """حفظ بيانات الامتحانات"""
        try:
            self.exams.to_csv("exams.csv", index=False, encoding='utf-8-sig', sep=';')
        except Exception as e:
            print(f"خطأ في حفظ الامتحانات: {e}")
    
    def load_exam_grades(self):
        """تحميل درجات الامتحانات"""
        try:
            if os.path.exists("exam_grades.csv"):
                self.exam_grades = pd.read_csv("exam_grades.csv", encoding='utf-8-sig', sep=';')
            else:
                self.exam_grades = pd.DataFrame(columns=["اسم_الامتحان", "اسم_الطالب", "الدرجة"])
        except Exception as e:
            print(f"خطأ في تحميل درجات الامتحانات: {e}")
            self.exam_grades = pd.DataFrame(columns=["اسم_الامتحان", "اسم_الطالب", "الدرجة"])
    
    def save_exam_grades(self):
        """حفظ درجات الامتحانات"""
        try:
            self.exam_grades.to_csv("exam_grades.csv", index=False, encoding='utf-8-sig', sep=';')
        except Exception as e:
            print(f"خطأ في حفظ درجات الامتحانات: {e}")
    
    def get_exam_grades(self, exam_name):
        """الحصول على درجات امتحان معين"""
        if not hasattr(self, 'exam_grades') or self.exam_grades.empty:
            return {}
        
        exam_data = self.exam_grades[self.exam_grades["اسم_الامتحان"] == exam_name]
        grades_dict = {}
        for _, row in exam_data.iterrows():
            grades_dict[row["اسم_الطالب"]] = row["الدرجة"]
        return grades_dict
    
    def save_student_grade(self, exam_name, student_name, grade):
        """حفظ درجة طالب في امتحان معين"""
        if not hasattr(self, 'exam_grades'):
            self.exam_grades = pd.DataFrame(columns=["اسم_الامتحان", "اسم_الطالب", "الدرجة"])
        
        # حذف الدرجة القديمة إذا وجدت
        self.exam_grades = self.exam_grades[
            ~((self.exam_grades["اسم_الامتحان"] == exam_name) & 
              (self.exam_grades["اسم_الطالب"] == student_name))
        ]
        
        # إضافة الدرجة الجديدة
        new_grade = pd.DataFrame({
            "اسم_الامتحان": [exam_name],
            "اسم_الطالب": [student_name],
            "الدرجة": [grade]
        })
        
        self.exam_grades = pd.concat([self.exam_grades, new_grade], ignore_index=True)
        self.save_exam_grades()
    
    def delete_exam_grades(self, exam_name):
        """حذف جميع درجات امتحان معين"""
        if hasattr(self, 'exam_grades') and not self.exam_grades.empty:
            self.exam_grades = self.exam_grades[self.exam_grades["اسم_الامتحان"] != exam_name]
            self.save_exam_grades()

    def send_exam_report(self, student_name, exam_name, grade, total_grade):
        """إرسال تقرير امتحان تلقائي عبر الواتساب"""
        try:
            # البحث عن بيانات الطالب
            student_data = self.students[self.students["الاسم"] == student_name]
            if student_data.empty:
                print(f"لم يتم العثور على بيانات الطالب: {student_name}")
                return
            
            student = student_data.iloc[0]
            phone = student.get("الهاتف", "")
            
            if not phone or str(phone).strip() == "nan":
                print(f"لا يوجد رقم هاتف للطالب: {student_name}")
                return
            
            # الحصول على تفاصيل الامتحان
            exam_details = self.get_exam_details(exam_name)
            
            # حساب النسبة المئوية
            percentage = (grade / total_grade) * 100
            
            # تحديد الحالة
            if percentage >= 50:
                status = "ناجح"
                status_emoji = "✅"
            else:
                status = "راسب"
                status_emoji = "❌"
            
            # إنشاء رسالة التقرير المحسنة
            message = f"""📊 تقرير امتحان {student_name}

🏫 تفاصيل الامتحان:
• اسم الامتحان: {exam_name}
• الصف: {exam_details.get('الصف', 'غير محدد')}
• التاريخ: {exam_details.get('التاريخ', 'غير محدد')}
• الوصف: {exam_details.get('الوصف', 'لا يوجد وصف')}

📝 النتيجة:
• الدرجة المحققة: {grade}/{total_grade}
• النسبة المئوية: {percentage:.1f}%
{status_emoji} الحالة: {status}

🎯 التقييم:
"""
            
            if percentage >= 90:
                message += "🌟 ممتاز! أداء رائع ومتفوق"
            elif percentage >= 80:
                message += "👍 جيد جداً! مستوى عالي من الفهم"
            elif percentage >= 70:
                message += "👌 جيد! أداء مقبول مع إمكانية التحسن"
            elif percentage >= 50:
                message += "⚠️ مقبول! يحتاج مزيد من الجهد والمراجعة"
            else:
                message += "🔴 يحتاج دعم إضافي وتحسين الأداء بشكل كبير"
            
            # إضافة نصائح حسب الأداء
            if percentage < 50:
                message += "\n\n💡 نصائح للتحسن:\n• المراجعة المستمرة للمادة\n• حل المزيد من التمارين\n• التواصل مع المعلم للاستفسار"
            elif percentage < 70:
                message += "\n\n💡 نصائح للتحسن:\n• التركيز على النقاط الضعيفة\n• المزيد من التدريب العملي"
            
            message += f"""

📞 معلومات التواصل:
• المعلم: أستاذ علي أبو بكر
• الهاتف: +201018603402

شكراً لثقتكم بنا 🌟"""
            
            # إرسال الرسالة
            success = send_whatsapp(phone, message)
            
            if success:
                print(f"✅ تم إرسال تقرير امتحان {exam_name} للطالب {student_name}")
            else:
                print(f"❌ فشل إرسال تقرير امتحان {exam_name} للطالب {student_name}")
                
        except Exception as e:
            print(f"خطأ في إرسال تقرير الامتحان: {str(e)}")
    
    def get_exam_details(self, exam_name):
        """الحصول على تفاصيل امتحان معين"""
        if hasattr(self, 'exams') and not self.exams.empty:
            exam_data = self.exams[self.exams["اسم_الامتحان"] == exam_name]
            if not exam_data.empty:
                exam_row = exam_data.iloc[0]
                return {
                    "اسم_الامتحان": exam_row["اسم_الامتحان"],
                    "الدرجة_الكلية": exam_row["الدرجة_الكلية"],
                    "التاريخ": exam_row["التاريخ"],
                    "الوصف": exam_row["الوصف"],
                    "الصف": exam_row["الصف"],
                    "الحالة": exam_row["الحالة"]
                }
        return {}
    
    def get_exam_date(self, exam_name):
        """الحصول على تاريخ امتحان معين"""
        if hasattr(self, 'exams') and not self.exams.empty:
            exam_data = self.exams[self.exams["اسم_الامتحان"] == exam_name]
            if not exam_data.empty:
                return exam_data.iloc[0]["التاريخ"]
        return "غير محدد"

if __name__ == "__main__":
    # إعداد دعم اللغة العربية قبل إنشاء النافذة
    try:
        import os
        os.environ['LANG'] = 'ar_EG.UTF-8'
        os.environ['LC_ALL'] = 'ar_EG.UTF-8'
    except:
        pass
    
    # إعداد Tkinter لدعم اللغة العربية
    try:
        root = tk.Tk()
        root.withdraw()  # إخفاء النافذة مؤقتاً
        
        # إعداد الخط الافتراضي
        root.option_add('*Font', 'SegoeUI 12')
        root.option_add('*Text.Font', 'SegoeUI 12')
        root.option_add('*Entry.Font', 'SegoeUI 12')
        root.option_add('*Label.Font', 'SegoeUI 12')
        root.option_add('*Button.Font', 'SegoeUI 12')
        
        root.deiconify()  # إظهار النافذة مرة أخرى
    except:
        root = tk.Tk()
    
    app = StudentNotifierApp(root)
    root.mainloop()
