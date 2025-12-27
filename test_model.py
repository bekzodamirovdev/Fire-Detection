# test_model.py - Run: python test_model.py

import os
import sys
import django

# Django setup
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from detector.utils import detector
import cv2
import numpy as np

print("\n" + "="*60)
print("🔥 FIRE DETECTION MODEL TEST")
print("="*60 + "\n")

# 1. Model mavjudligini tekshirish
print("1️⃣ Model Status:")
if detector.model:
    print("   ✅ Model yuklandi")
    print(f"   📁 Model type: {type(detector.model)}")
else:
    print("   ❌ Model yuklanmadi")
    sys.exit(1)

# 2. Model classlarini ko'rish
print("\n2️⃣ Model Classes:")
if hasattr(detector.model, 'names'):
    print(f"   Classes: {detector.model.names}")
else:
    print("   ⚠️ Model.names mavjud emas")

# 3. Test rasm yaratish va inference
print("\n3️⃣ Test Inference:")
try:
    # Qizil test rasm (fire ni simulate qilish)
    test_img = np.zeros((640, 640, 3), dtype=np.uint8)
    test_img[200:400, 200:400] = [0, 0, 255]  # Qizil kvadrat
    
    print("   🔄 Inference ishlamoqda...")
    results = detector.model(test_img, conf=0.25, verbose=False)
    
    print(f"   ✅ Inference muvaffaqiyatli")
    print(f"   📊 Results type: {type(results)}")
    print(f"   📦 Results length: {len(results)}")
    
    # Natijalarni tekshirish
    for i, result in enumerate(results):
        print(f"\n   Result {i}:")
        print(f"      - Has boxes: {hasattr(result, 'boxes')}")
        if hasattr(result, 'boxes') and result.boxes is not None:
            print(f"      - Number of boxes: {len(result.boxes)}")
            if len(result.boxes) > 0:
                for j, box in enumerate(result.boxes[:3]):  # Faqat birinchi 3 ta
                    conf = float(box.conf[0])
                    cls = int(box.cls[0])
                    print(f"      - Box {j}: conf={conf:.3f}, class={cls}")
        
except Exception as e:
    print(f"   ❌ Inference xatosi: {e}")
    import traceback
    traceback.print_exc()

# 4. Real fayl bilan test (agar mavjud bo'lsa)
print("\n4️⃣ File Detection Test:")
test_files = ['test.jpg', 'test.png', 'fire.jpg']
found_test_file = None

for filename in test_files:
    if os.path.exists(filename):
        found_test_file = filename
        break

if found_test_file:
    print(f"   📁 Test fayl topildi: {found_test_file}")
    try:
        fire_detected, confidence, result_img = detector.detect_fire(found_test_file)
        print(f"   🔍 Detection result:")
        print(f"      - Fire detected: {fire_detected}")
        print(f"      - Confidence: {confidence:.3f}")
        print(f"      - Result image: {result_img is not None}")
    except Exception as e:
        print(f"   ❌ Detection xatosi: {e}")
else:
    print("   ℹ️ Test fayl topilmadi (test.jpg, test.png, fire.jpg)")
    print("   💡 Test uchun rasmni loyiha katalogiga qo'ying")

print("\n" + "="*60)
print("✅ TEST TUGADI")
print("="*60 + "\n")