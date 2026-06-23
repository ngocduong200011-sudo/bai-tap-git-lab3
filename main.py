def tinh_diem_gpa(diem_so):
    # Công thức tuyến tính đơn giản của Dev A
    return round((diem_so/10) * 4, 2)
    if diem_so >= 8.5: return 4.0
    elif diem_so >= 7.0: return 3.0
    else: return 2.0

print("Điểm GPA hệ 4 là:", tinh_diem_gpa(8.5))