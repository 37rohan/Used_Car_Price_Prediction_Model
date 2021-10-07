import streamlit as st
from PIL import Image
def app(df):
    
    st.balloons()
    st.title("Contributers of This Project")

    col1,col2,col3 = st.columns(3)

    with col1:
        img = Image.open("rohan.jpg")
        st.image(img,width=200)
        st.markdown("#### Name: ")
        st.text("Rohan Goyal")

        st.markdown("""#### College:""")
        st.text("Poornima University")

        st.markdown("""#### Branch:""")
        st.text("BCA(DS)")
                
        st.markdown("""#### Github:""")
        st.markdown("[Rohan Goyal](https://github.com/37rohan)")

        st.markdown("""#### LinkedIn:""")
        st.markdown("[Rohan Goyal](https://www.linkedin.com/in/rohan-goyal-3a1744200/)")
    
    with col2:
        img = Image.open("khushi.jpg")
        st.image(img,width=200)
        st.markdown("#### Name: ")
        st.text("Khushi Singhal")

        st.markdown("""#### College:""")
        st.text("Poornima University")

        st.markdown("""#### Branch:""")
        st.text("BCA(Gen.)")

        st.markdown("""#### Github:""")
        st.markdown("""[Khushi Singhal](https://github.com/misskhushi)""")

        st.markdown("""#### LinkedIn:""")
        st.markdown("""[Khushi Singhal](https://www.linkedin.com/in/khushi-singhal-042b18210/)""")

    with col3:    
        img = Image.open("priyanshu.jpg")
        st.image(img,width=200)
        st.markdown("#### Name: ")
        st.text("Priyanshu Kumar")

        st.markdown("""#### College:""")
        st.text("Poornima University")

        st.markdown("""#### Branch:""")
        st.text("BCA(AI)")

        st.markdown("""#### Github:""")
        st.markdown("""[Priyanshu Kumar](https://github.com/Priyanshu6378)""")

        st.markdown("""#### LinkedIn:""")
        st.markdown("""[Priyanshu Kumar](https://www.linkedin.com/in/priyanshu-kumar-592a90200/)""")
