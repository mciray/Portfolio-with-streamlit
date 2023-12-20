import streamlit as st
import requests
from datetime import datetime
import time
from annotated_text import annotated_text
from streamlit_monaco import st_monaco
import subprocess
import os

def get_github_repos(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url) 
    if response.status_code == 200:
        return response.json()
    else:
        return []
def get_github_repo_files(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/contents/"
    response = requests.get(url)
    if response.status_code == 200:
      
        return response.json()
    else:
        return []


def display_repo_card(repo):
    # Repo bilgilerini formatla
    repo_name = repo['name']
    description = repo['description'] or 'Açıklama yok'
    stars = repo['stargazers_count']
    language = repo['language'] or 'Bilgi yok'
    updated_at = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ").strftime("%d %b, %Y")
    repo_url = repo['html_url']

    # Kartı oluştur
    st.markdown(f"""
    <div style="margin: 10px; padding: 10px; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,.1);">
        <h3 style="margin: 0;">{repo_name}</h3>
        <p>{description}</p>
        <p>⭐ {stars} | 💻 {language} | 📅 Son Güncelleme: {updated_at}</p>
        <a href="{repo_url}" target="_blank">Repo'ya Git</a>
    </div>
    """, unsafe_allow_html=True)


def main():
   
    st.title("Melih Çıray")

    st.sidebar.title("Navigasyon")
    st.sidebar.markdown("## Bölümler")
    
    # Navigasyon
    page = st.sidebar.radio("Sayfaları Seçin", ["Hakkımda", "Projeler", "İletişim"])

    if page == "Hakkımda":
      

        st.image("foto.jpg", width=300, caption="Ben, Melih Çıray")
        st.markdown("<div><h3>hakkımda</h3><div>",unsafe_allow_html=True)
        st.markdown("""
            <div> <div><ul>
            <li>Merhaba, ben Melih Çıray &#128075;</li>
            <li>Back-End Developer'ım. &#128187;</li>
            <li>22 yaşındayım ve şu anda Baykar'da back-end developer olarak staj yapıyorum. </li>
            <li>Bilgisayar Programcılığı alanında İstinye Üniversitesi'nden mezun oldum ve şu anda Anadolu Üniversitesi Yönetim Bilişim Sistemleri bölümünde 4. sınıf öğrencisiyim. &#128210;</li>
            <li>İstanbul'da yaşıyorum.  &#128205;</li>
          
        </ul></div> </div> 
           
        """, unsafe_allow_html=True)
        data = [
            ("container", "Docker"),
            ("Python", "Django"),
            ("Python", "Django Rest Framework"),
            ("Redis", "Celery"),
            ("Javascript", "Node.js"),
            ("Javascript", "Jquery"),
        ]     
        st.write("İşte kullandığım bazı teknolojiler:")
        annotated_text(
                *data[:len(data)//1:]
        )
        javascript_code = st_monaco(value="//JavaScript", height="300px",  language="javascript")

        if st.button("Run"):
            try:
                # JavaScript kodunu temp.js dosyasına yaz
                with open("temp.js", "w") as temp_file:
                    temp_file.write(javascript_code)

                # node.exe yolu. Projenizin yapısına göre bu yolu güncelleyin.
                node_exe_path = "./node.exe"
                os.chmod(node_exe_path, 744)
                # subprocess.check_output ile JavaScript dosyasını çalıştır
                result = subprocess.check_output([node_exe_path, "temp.js"], text=True)

                # Çıktıyı göster
                st.text("Output:")
                st.code(result, language="javascript")
                        
            except Exception as e:
                st.error(f"Error: {str(e)}")
            
    # Projeler
    elif page == "Projeler":
        st.balloons()
        st.markdown("""
                <div style='text-align: center;height:300px;'>
                    <img src='https://pridesys.com/wp-content/uploads/2022/09/programming-web-banner-best-programming-languages-technology-process-of-software-development-700-175188152.jpg' style="object-fit:cover;height:300px;width:100%;">
                </div>
    """, unsafe_allow_html=True)
      
        st.header("Projelerim")
        st.write("Burada, geliştirdiğim projeler ve çalışmalar hakkında bilgileri bulabilirsiniz.")
        col1,col2 = st.columns(2)
        col1.write("streamlit ile yaptığım basit bir havadurumu uygulaması:")
        col2.write(" https://app-weather-app-ciray.streamlit.app/ ")
        st.subheader("GitHub Projelerim")
        username = "mciray"  # GitHub kullanıcı adınız
        repos = get_github_repos(username)
        if repos:
            for repo in repos:
                display_repo_card(repo)
               
               
        else:
            st.write("Repo bulunamadı veya bir hata oluştu.")
            # Diğer proje bilgileri buraya eklenebilir.

    # İletişim
    elif page == "İletişim":
        
        st.markdown("<div><h3>İletişim Bilgileri &#128227;</h3></div>", unsafe_allow_html=True)
        st.write("Benimle iletişime geçmek için aşağıdaki adresleri kullanabilirsiniz:")
        st.markdown("<div><p> &#128234;</p></div>",unsafe_allow_html=True)
        st.write("E-posta: [melihciray@gmail.com](mailto:melihciray@gmail.com)")
        # LinkedIn bağlantısı
        st.markdown("<div>&#128231;</div>", unsafe_allow_html=True)
        linkedin_link = "https://www.linkedin.com/in/melihciray/"
        st.write("LinkedIn: [Melih Çıray LinkedIn](" + linkedin_link + ")")

        # Instagram bağlantısı
        st.markdown("<div>&#128640;</div>", unsafe_allow_html=True)
        instagram_link = "https://www.instagram.com/melihcray/"
        st.write("Instagram: [Melih Çıray Instagram](" + instagram_link + ") :camera:")

        # GitHub bağlantısı
        st.markdown("<div>&#128187;</div>", unsafe_allow_html=True)
        github_link = "https://github.com/mciray"
        st.write("GitHub: [Melih Çıray GitHub](" + github_link + ")")
       

   
        # LinkedIn, GitHub gibi diğer sosyal medya bağlantıları eklenebilir.

if __name__ == "__main__":
    main()
