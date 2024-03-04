import streamlit as st
from PIL import Image
import base64

bg_image_path = "streamlit/All Pictures/bg02.jpg"
with open(bg_image_path, "rb") as img_file:
    bg_image = img_file.read()
bg_image_base64 = base64.b64encode(bg_image).decode()
page_bg_img = f'''
    <style>
        .stApp {{
            background-image: url("data:image/png;base64,{bg_image_base64}");
            background-size: cover;
        }}
    </style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)




def main():
    menu1 = [" 🏠 HOME", "🎵 MUSIC ", " 📅 EVENTS", "🛒 ONLINE SHOP ", " 📞 CONTACT"]
    choice = st.sidebar.selectbox('Menu', menu1)

    if  choice == ' 🏠 HOME':
        
        html_content = """
        <div style='text-align: center;'>
            <h3>FANPAGE BTS (방탄소년단)</h3>
    """
        st.write(html_content, unsafe_allow_html=True)
        logo = Image.open("streamlit/All Pictures/bts1.jpg")
        logo_rs = logo.resize((800, 500))
        st.image(logo_rs, use_column_width=False)

        st.markdown('')
        st.markdown('')
        html_content = """
        <div style='text-align: center;'>
            <h3>MEMBER</h3>
    """
        st.write(html_content, unsafe_allow_html=True)

        st.markdown('')
        st.markdown('')

        col1, col2 = st.columns(2)
        col1.image('streamlit/All Pictures/m01.jpg')
        col2.markdown('')
        col2.markdown('')
        col2.subheader('RM')
        col2.write('ชื่อจริง : คิม นัมจุน (Kim Nam Joon) (김남준)')
        col2.write('ตำแหน่ง : Leader, Main Rapper')
        col2.write('วันเกิด : 12 กันยายน 1994')
        col2.write('บ้านเกิด : อิลซาน จังหวัดคยองกี ประเทศเกาหลีใต้')
        col2.write('สัญชาติ : เกาหลีใต้')
        col2.write('สูง : 181 cm')
        col2.write('น้ำหนัก : 64 kg')
        col2.write('หมู่เลือด : A')
        col2.markdown("Spotify list : [RM’s Favorite Tracks](https://open.spotify.com/playlist/0brZe9voOPUysDkWVCOATf)")
        col2.markdown("INSTAGRAM : [rkive](https://www.instagram.com/rkive/)")
        st.markdown('')
        st.markdown('')
        
        col1, col2 = st.columns(2)
        col1.image('streamlit/All Pictures/m02.jpg')
        col2.markdown('')
        col2.markdown('')
        col2.subheader('JIN')
        col2.write('ชื่อจริง : คิม ซอกจิน (Kim Seok Jin) (김석진)')
        col2.write('ตำแหน่ง : นักร้องเสริม, ภาพลักษณ์, พี่ใหญ่')
        col2.write('วันเกิด : 4 ธันวาคม 1992')
        col2.write('บ้านเกิด : กวาชอน จังหวัดคยองกี ประเทศเกาหลีใต้')
        col2.write('สัญชาติ : เกาหลีใต้')
        col2.write('สูง : 179 cm')
        col2.write('น้ำหนัก : 60 kg')
        col2.write('หมู่เลือด : O')
        col2.markdown("Spotify list : [Jin’s Favorite Tracks](https://https://open.spotify.com/playlist/3wcvwNITmfb6sC6MKEJVX9)")
        col2.markdown("INSTAGRAM : [jin](https://www.instagram.com/jin/)")
        st.markdown('')
        st.markdown('')
        
        col1, col2 = st.columns(2)
        col1.image('streamlit/All Pictures/m03.jpg')
        col2.markdown('')
        col2.markdown('')
        col2.subheader('SUGA')
        col2.write('ชื่อจริง : มิน ยุนกิ (Min Yoon Gi) (민윤기)')
        col2.write('ตำแหน่ง : แร็ปเปอร์หลัก')
        col2.write('วันเกิด : 9 มีนาคม 1993')
        col2.write('บ้านเกิด : แทกู ประเทศเกาหลีใต้')
        col2.write('สัญชาติ : เกาหลีใต้')
        col2.write('สูง : 174 cm')
        col2.write('น้ำหนัก : 57 kg')
        col2.write('หมู่เลือด : O')
        col2.markdown("Spotify list : [ SUGA’s Favorite Tracks](https://open.spotify.com/playlist/2FzWRo9ImvPMa7iAL9jCKF)")
        col2.markdown("INSTAGRAM : [agustd](https://www.instagram.com/agustd/)")
        st.markdown('')
        st.markdown('')
        
        col1, col2 = st.columns(2)
        col1.image('streamlit/All Pictures/m04.jpg')
        col2.markdown('')
        col2.markdown('')
        col2.subheader('J-HOPE')
        col2.write('ชื่อจริง : ชอง โฮซอก (Jung Ho Seok) (정호석)')
        col2.write('ตำแหน่ง : นักเต้นหลัก, แร็ปเปอร์นำ')
        col2.write('วันเกิด : 18 กุมภาพันธ์ 1994')
        col2.write('บ้านเกิด : ควังจู ประเทศเกาหลีใต้')
        col2.write('สัญชาติ : เกาหลีใต้')
        col2.write('สูง : 177 cm')
        col2.write('น้ำหนัก : 59 kg')
        col2.write('หมู่เลือด : A')
        col2.markdown("Spotify list : [ J-Hope’s Favorite Tracks](https://open.spotify.com/playlist/6KdDdkjD5I3ObRqrc4TKNt)")
        col2.markdown("INSTAGRAM : [uarmyhope](https://www.instagram.com/uarmyhope/)")
        st.markdown('')
        st.markdown('')

        col1, col2 = st.columns(2)
        col1.image('streamlit/All Pictures/m05.jpg')
        col2.markdown('')
        col2.markdown('')
        col2.subheader('JIMIN')
        col2.write('ชื่อจริง : ปาร์ค จีมิน (Park Ji Min) (박지민)')
        col2.write('ตำแหน่ง : นักเต้นนำ, นักร้องนำ')
        col2.write('วันเกิด : 13 ตุลาคม 1995')
        col2.write('บ้านเกิด : ปูซาน ประเทศเกาหลีใต้')
        col2.write('สัญชาติ : เกาหลีใต้')
        col2.write('สูง : 173 cm')
        col2.write('น้ำหนัก : 60 kg')
        col2.write('หมู่เลือด : A')
        col2.markdown("Spotify list : [ Jimin’s Favorite Tracks](https://open.spotify.com/playlist/0brZe9voOPUysDkWVCOATf)")
        col2.markdown("INSTAGRAM : [j.m](https://www.instagram.com/j.m/)")
        st.markdown('')
        st.markdown('')

        col1, col2 = st.columns(2)
        col1.image('streamlit/All Pictures/m06.jpg')
        col2.markdown('')
        col2.markdown('')
        col2.subheader('V')
        col2.write('ชื่อจริง : คิม แท ฮยอง (Kim Tae Hyung) (김태형)')
        col2.write('ตำแหน่ง : นักร้องนำ, ภาพลักษณ์')
        col2.write('วันเกิด : 30 ธันวาคม 1995')
        col2.write('บ้านเกิด : แทกู ประเทศเกาหลีใต้')
        col2.write('สัญชาติ : เกาหลีใต้')
        col2.write('สูง : 178 cm')
        col2.write('น้ำหนัก : 63 kg')
        col2.write('หมู่เลือด : AB')
        col2.markdown("Spotify list : [V’s Favorite Tracks](https://open.spotify.com/playlist/2nKFSE6yJw9Xh2uDKzwmZb)")
        col2.markdown("INSTAGRAM : [thv](hhttps://www.instagram.com/thv/)")

        col1, col2 = st.columns(2)
        col1.image('streamlit/All Pictures/m07.jpg')
        col2.markdown('')
        col2.markdown('')
        col2.subheader('JUNGKOOK')
        col2.write('ชื่อจริง : จอน จองกุก (Jeon Jeong-guk) (전정국)')
        col2.write('ตำแหน่ง : นักร้องเสียงหลัก, นักเต้นนำ, แร็ปเปอร์เสริม, เซ็นเตอร์, น้องเล็ก')
        col2.write('วันเกิด : 1 กันยายน 1997')
        col2.write('บ้านเกิด : ปูซาน  ประเทศเกาหลีใต้')
        col2.write('สัญชาติ : เกาหลีใต้')
        col2.write('สูง : 178 cm')
        col2.write('น้ำหนัก : 61 kg')
        col2.write('หมู่เลือด : A')
        col2.markdown("Spotify list : [ Jungkook's Favorite Tracks](https://open.spotify.com/playlist/59b6qZDNJI2ZfhqZFMaU6R)")
        col2.markdown("INSTAGRAM : -")

        st.markdown('')
        st.markdown('')
        st.subheader('LINKS')
        st.markdown("[MUSIC](https://www.youtube.com/results?search_query=bts)")
        st.markdown("[ONLINE SHOP](https://weverseshop.io/en/shop/GL_USD/artists/2/categories/175)")
        st.markdown("[INSTAGRAM](https://www.instagram.com/bts.bighitofficial/)")
        st.markdown("[TWITTER](https://twitter.com/bts_bighit)")

    elif choice == '🎵 MUSIC ':
        html_content = """
        <div style='text-align: center;'>
            <h3>NEW ALBUM!</h3>
    """
        st.write(html_content, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        st.markdown('')
        st.markdown('')  
        col1.subheader('Album')
        col1.markdown("[1.Life Goes On](https://www.youtube.com/watch?v=-5q5mZbe3V8)")
        col1.markdown("[2.Fly To My Room](https://www.youtube.com/watch?v=YSuOwf24psk)")
        col1.markdown("[3.Blue & Grey](https://www.youtube.com/watch?v=KCssqGPEWvM)")
        col1.markdown("[4.Skit](https://www.youtube.com/watch?v=YkGEbnNj48k)")
        col1.markdown("[5.Telepathy](https://www.youtube.com/watch?v=OGMeHzBLuM8)")
        col1.markdown("[6.Dis-ease](https://www.youtube.com/watch?v=rSi4UIWbtM0)")
        col1.markdown("[7.Stay](https://www.youtube.com/watch?v=evBAiaYal1o)")
        col1.markdown("[8.Dynamite](https://www.youtube.com/watch?v=gdZLi9oWNZg)")
        
        col2.markdown('')
        col2.markdown('')
        col2.markdown('')
        col2.markdown('')
        col2.markdown('')
        col2.video('https://www.youtube.com/watch?v=-5q5mZbe3V8')

    elif choice == ' 📅 EVENTS':
        html_content = """
        <div style='text-align: center;'>
            <h3>CONCERT TOUR</h3>
    """
        st.write(html_content, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        col1.header('June 10st')
        col2.subheader('Concert Venue')
        col2.markdown('Thailand')
        col3.subheader('Concert Time')
        col3.write('6pm-9pm')
        st.markdown('')
        st.markdown('')

        col1, col2, col3 = st.columns(3)
        col1.header('June 16st')
        col2.subheader('Concert Venue')
        col2.write('Japan')
        col3.subheader('Concert Time')
        col3.write('7pm-10pm')
        st.markdown('')
        st.markdown('')

        col1, col2, col3 = st.columns(3)
        col1.header('June 21st')
        col2.subheader('Concert Venue')
        col2.write('South Korea')
        col3.subheader('Concert Time')
        col3.write('5pm-8pm')

    elif choice == '🛒 ONLINE SHOP ':
        html_content = """
        <div style='text-align: center;'>
            <h3>ONLINE SHOP</h3>
    """
        st.write(html_content, unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        original1 = Image.open("streamlit/All Pictures/bts001.png")
        col1.image(original1, caption="Mikrokosmos Mood Lamp   $900", use_column_width=True)
        original2 = Image.open("streamlit/All Pictures/bts002.jpg")
        col2.image(original2, caption="beWATER with BTS  $650", use_column_width=True)
        original3 = Image.open("streamlit/All Pictures/bts003.jpg")
        col3.image(original3, caption="Mug Cup 02   $400", use_column_width=True)
        col1, col2, col3 = st.columns(3)
        original1 = Image.open("streamlit/All Pictures/bts004.jpg")
        col1.image(original1, caption="ficial Light Stick Special Edition   $1399", use_column_width=True)
        original2 = Image.open("streamlit/All Pictures/bts005.jpg")
        col2.image(original2, caption="Bucket Hat   $309", use_column_width=True)
        original3 = Image.open("streamlit/All Pictures/bts006.png")
        col3.image(original3, caption="Strap Keyring    $329", use_column_width=True)

    elif choice == ' 📞 CONTACT':
        html_content = """
        <div style='text-align: center;'>
            <h3>MEMBERSHIP</h3>
    """
        st.write(html_content, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col1.markdown('')
        col1.subheader('FANPAGE BTS (방탄소년단)')
        col1.text('This work was created by')
        col1.subheader('PRATTHANA  DAVONG')
        col1.text('[phone]')
        col1.markdown('[pratthana.da.66@ubu.ac.th](pratthana.da.66@ubu.ac.th)')
        col2.image('streamlit/All Pictures/b01.png')

        st.markdown('')
        st.markdown('')
        html_content = """
        <div style='text-align: center;'>
            <h3>VIP List</h3>
            <p>Sign up to get early access to tickets and upcoming events.</p>
    """
        st.write(html_content, unsafe_allow_html=True)
        st.subheader("Create Account")
        st.write("Create a new account here.")
        first_name = st.text_input("First name")
        last_name = st.text_input("Last name")
        email = st.text_input("Email")
        phone = st.text_input("Phone(optional)")
        new_password = st.text_input("Password", type='password')

        if st.button("Create Account"):
            st.success("You have successfully created a valid account.")
            st.info("Proceed to login to access your account.")


if __name__ == "__main__":
    main()