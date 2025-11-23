from PIL import Image, ImageDraw, ImageFont
import random

## 메인 사진 
def draw_rounded_text(draw, xy, text, font, padding, bg_color, text_color, radius):
    x, y = xy
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    box = [x, y, x + w + padding*2, y + h + padding*2]
    draw.rounded_rectangle(box, radius=radius, fill=bg_color)
    draw.text((x + padding, y + padding), text, font=font, fill=text_color)
    return box[2], box[3]

def create_template_image(
    small_text,
    main_text
):
    img = Image.open("./1.jpeg").convert("RGB")
    draw = ImageDraw.Draw(img)

    font_small = ImageFont.truetype("./ttf/Hakgyoansim_TteokbokkiB.ttf", 200)
    font_main = ImageFont.truetype("./ttf/Hakgyoansim Allimjang TTF B.ttf", 380)

    width, height = img.size

    padding = 80
    radius = 150
    x = 100
    y = height - 1100
    draw_rounded_text(draw, (x, y-200), small_text, font_small, padding, bg_color="#dcead0", text_color="#518233", radius=radius)

    bbox_small = draw.textbbox((0, 0), small_text, font=font_small)
    small_height = bbox_small[3] - bbox_small[1]
    y_main = y + small_height + 20  # 20 px gap

    # 문자 삽입
    draw.text(
            (x, y_main),  # 위치
            main_text,  # 문구
            font=font_main,  # 폰트종류, 폰트크기
            fill="#b0d484",  # 문자색
            stroke_width=8,  # 테투리 두께
            stroke_fill="#4d4f3f",  # 테두리 색
            align='left',  # 정렬
            spacing=80  # 라인간 공백
        )
    img.save('./main.jpeg')



## BEFORE & AFTER
def draw_rounded_text2(draw, xy, text, font, padding, bg_color, text_color, radius):
    x, y = xy
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    box = [x-100, y, x + w + padding*4, y + h + padding*2]
    draw.rounded_rectangle(box, radius=radius, fill=bg_color)
    draw.text((x + padding, y + padding), text, font=font, fill=text_color, align='center')
    return box[2], box[3]

def create_template_image_before_after(
    image_name
    , small_text
):
    img = Image.open(image_name).convert("RGB")
    draw = ImageDraw.Draw(img)

    font_small = ImageFont.truetype("./ttf/Hakgyoansim Allimjang TTF B.ttf", 190)
    
    width, height = img.size

    padding = 80
    radius = 150
    x = width / 2 - 350 
    y = height - 500
    draw_rounded_text2(draw, (x, y), small_text, font_small, padding, bg_color="#dcead0", text_color="#518233", radius=radius)

    img.save('./'+small_text+'.jpeg')

def create_location_file(): 
    # 서울 동 리스트 뽑기 
    with open("./dong_list/seoul.txt", "r", encoding="utf-8") as f:
        seoul_dong_list = [line.strip() for line in f if line.strip()]

    random_selection = random.sample(seoul_dong_list, 8) 

    text_to_write = ", ".join(random_selection)
    text_to_write+=" 등\n"
    text_to_write+= "(서울 전 지역 출장 가능)\n\n"

    # 경기 동 리스트 뽑기
    with open("./dong_list/gyeonggido.txt", "r", encoding="utf-8") as f:
        gyeonggi_dong_list = [line.strip() for line in f if line.strip()]

    random_selection = random.sample(gyeonggi_dong_list, 8) 

    text_to_write+= ", ".join(random_selection)
    text_to_write+=" 등\n"
    text_to_write+= "(경기 전 지역 출장 가능)\n\n"

    # 인천 동 리스트 뽑기
    with open("./dong_list/incheon.txt", "r", encoding="utf-8") as f:
        inchoen_dong_list = [line.strip() for line in f if line.strip()]

    random_selection = random.sample(inchoen_dong_list, 8)  

    text_to_write+= ", ".join(random_selection)
    text_to_write+=" 등\n"
    text_to_write+= "(인천 전 지역 출장 가능)\n\n"

    with open("random_dong.txt", "w") as file:
        file.write(text_to_write)

    print(f"Generated text file with: {text_to_write}")

if __name__ == "__main__":
    print("=== Command-Line Image Editor ===")
    title1 = input("제목 입력하기!!! (줄바꾸기는 \n 넣기)): ").strip()
    title1 = title1.replace("\\n", "\n")


    create_template_image('집수리의 모든 것! 일품집수리',title1)
    create_template_image_before_after("./2.jpeg", "작업 전")
    create_template_image_before_after("./3.jpeg", "작업 후")
    create_location_file()

    