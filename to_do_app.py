import streamlit as st

st.set_page_config(
    page_title='To-Do List',
    page_icon='✅',
    layout = 'centered'
)

st.title("📝 나의 할일 목록", anchor='title-section',help="anchor 존재")
# st.markdown("# 📝 나의 할일 목록")
# st.markdown("# [📝 나의 할일 목록](https://www.google.com)")

st.write("간단하고 효율적인 할일 관리를 시작해보세요!")

st.header("📖 사용법")
# st.markdown("## 📖 사용법")
# st.header("📖 사용법2",divider='red')
# st.header("📖 사용법3",divider=True)
# st.header("📖 사용법4",divider=True)
# st.header("📖 사용법5",divider=True)

# st.subheader('1. 할일 추가', anchor='subheader-section',help="subheader 존재")
# st.markdown("### 1. 할일 추가")
# st.subheader('2. 완료 표시')
# st.subheader('3. 할일 삭제')
# st.subheader('4. 일괄 관리', anchor='subheader-section2',help="subheader 존재2")

st.write("""
1. **할일 추가**: 텍스트 입력 후 '추가하기' 버튼 클릭 \n
2. **완료 표시**: 체크박스를 클릭하여 완료 표시 \n
3. **할일 삭제**: 🗑️ 버튼으로 개별 삭제 \n
4. **일괄 관리**: 완료된 할일만 삭제하거나 전체 삭제
""")

# st.caption('안녕하세요.', help='캡션입니다.')
# st.caption('안녕하세요. <font size=16>환영합니다.</font>'
# ,unsafe_allow_html=True
# ,help='캡션입니다.') # 마크다운에서도 HTML 적용 가능
# st.caption('안녕하세요. <font size=16>환영합니다.</font>'
# ,help='캡션입니다.')

# st.code('import streamlit as st')
# st.code('''import streamlit as st
# a=st.button('안녕')
# if a:
#     st.text('버튼클릭')
# else:
#     st.text('버튼클릭안함')st.text('버튼클릭안함')st.text('버튼클릭안함')'''
#     , height=70, line_numbers=True,wrap_lines=True)
# st.code('<font size=16>환영합니다.</font>', language='html')

# st.divider()

# with st.echo():
#     num = 1+1
#     st.write(num)
    
# def get_user_name():
#     return 'jin'

# with st.echo():
#     def get_p():
#         return '!!!'
    
#     g='안녕, '
#     v= get_user_name()
#     p= get_p()

#     st.write(g,v,p)

# st.write('잘가')

# st.latex(r'ax^2 + bx + c = 0', help='2차 방정식')
# st.text('안녕하세요.', help='텍스트입니다.')
# st.help()
# import pandas as pd
# import numpy as np

# df = pd.DataFrame(np.random.randn(200,3)
# ,columns=['a','b','c'])
# st.help(df)
# st.html('<font size=16>환영합니다.</font>')

def custom_warning(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #ff6b35;
        background-color: var(--warning-bg, #fff3cd);
        border-radius: 0.25rem;
        color: var(--warning-text, #856404);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --warning-bg: #3d2914;
                --warning-text: #ffcc02;
            }}
        }}
        [data-theme="dark"] {{
            --warning-bg: #3d2914;
            --warning-text: #ffcc02;
        }}
    </style>
    """, unsafe_allow_html=True)

def custom_success(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #28a745;
        background-color: var(--success-bg, #d4edda);
        border-radius: 0.25rem;
        color: var(--success-text, #155724);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --success-bg: #1e3a24;
                --success-text: #4caf50;
            }}
        }}
        [data-theme="dark"] {{
            --success-bg: #1e3a24;
            --success-text: #4caf50;
        }}
    </style>
    """, unsafe_allow_html=True)

def custom_info(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #17a2b8;
        background-color: var(--info-bg, #d1ecf1);
        border-radius: 0.25rem;
        color: var(--info-text, #0c5460);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --info-bg: #0d2a3a;
                --info-text: #5bc0de;
            }}
        }}
        [data-theme="dark"] {{
            --info-bg: #0d2a3a;
            --info-text: #5bc0de;
        }}
    </style>
    """, unsafe_allow_html=True)

def custom_error(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #dc3545;
        background-color: var(--error-bg, #f8d7da);
        border-radius: 0.25rem;
        color: var(--error-text, #721c24);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --error-bg: #3a1a1d;
                --error-text: #f44336;
            }}
        }}
        [data-theme="dark"] {{
            --error-bg: #3a1a1d;
            --error-text: #f44336;
        }}
    </style>
    """, unsafe_allow_html=True)

# custom_error('에러입니다.')
# st.error('에러입니다.')
st.subheader('➕ 새로운 할일 추가')

new_todo = st.text_input('할일을 입력하세요 : ',
placeholder = '예: 장보기, 운동하기, 책 읽기')

submitted = st.button('추가하기')

if 'todos' not in st.session_state:
    st.session_state.todos = []

if submitted:
    if new_todo.strip(): # 빈문자열이 아닌지 판단을 하는 함수
        st.session_state.todos.append({
            'tast':new_todo.strip(),
            'completed':False
        })
        custom_success(f"✅ '{new_todo}'가 추가되었습니다!")
    else:
        custom_warning('⚠️ 할일을 입력해주세요.')

st.divider()

st.subheader('📕 할일 목록')

# st.write(st.session_state.todos)

if st.session_state.todos:
    for i in reversed(range(len(st.session_state.todos))):
        todo=st.session_state.todos[i]

        col1,col2,col3 = st.columns([0.1,0.7,0.2])
        
        with col1:
            completed=st.checkbox("",
            value=todo['completed'],
            key=f"check_{i}",
            help='완료 체크')

            if completed!=todo['completed']:
                st.session_state.todos[i]['completed']=completed
                st.rerun()
                # st.write('???')

        with col2:
            if completed:
                st.markdown(f"~~{todo['tast']}~~", help='완료된 할일')
            else:
                st.write(todo['tast'])

        with col3:
            if st.button("🗑️",key=f"delete_{i}", help="삭제"):
                st.session_state.todos.pop(i)
                custom_success("삭제되었습니다!")
                st.rerun()

        if i>=0:
            st.markdown('---')
else:
    custom_info("👉 아직 할일이 없습니다. \
    새로운 할일을 추가해보세요!")

if st.session_state.todos:
    total_todos=len(st.session_state.todos)
    completed_todos = 0

    for i in st.session_state.todos:
        if i['completed']:
            completed_todos +=1
    remaining_tods=total_todos-completed_todos
    if total_todos>0:
        completion_rate = (completed_todos/total_todos*100)
    else:
        completion_rate=0

    col1, col2= st.columns(2)

    with col1:
        if st.button("🗑️모든 할일 삭제",type="secondary"):
            st.session_state.todos=[]
            custom_success("모든 할일이 삭제되었습니다.")
            st.rerun()
    with col2:
        if completed_todos>0:
            if st.button(f"✅완료된 할일 {completed_todos}개 삭제",type="secondary"):
                todo_list=[]
                for i in st.session_state.todos:
                    if not i['completed']:
                        todo_list.append(i)
                st.session_state.todos=todo_list
                custom_success("완료된 할일 {completed_todos}개가 삭제되었습니다.")
                st.rerun()
    st.subheader("📊통계")

    def display_stat(title,value,delta=None,value_color=None):
        delta_str=""
        if delta is not None:
            if delta>0:
                delta_str=f"(⬆️{delta})"
            elif delta<0:
                delta_str=f"(⬇️{delta})"
            else:
                delta_str=""

        if value_color is None:
            value_color="var(--text-color, #262730)"

        st.markdown(f"""
            <div style="
                padding: 1rem; 
                background-color: var(--stat-bg, #f0f2f6); 
                border: 1px solid var(--stat-border, transparent);
                border-radius: 10px; 
                text-align: center;
                box-shadow: var(--stat-shadow, 0 1px 3px rgba(0,0,0,0.1));
            ">
                <div style="
                    font-size: 18px; 
                    font-weight: bold; 
                    color: var(--title-color, #262730);
                    margin-bottom: 0.5rem;
                ">{title}</div>
                <div style="
                    font-size: 32px; 
                    font-weight: bold; 
                    color: {value_color};
                ">{value}{delta_str}</div>
            </div>
            <style>
                /* 라이트모드 기본값 */
                :root {{
                    --stat-bg: #f0f2f6;
                    --stat-border: transparent;
                    --stat-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    --title-color: #262730;
                    --text-color: #262730;
                }}
                
                /* 다크모드 스타일 */
                @media (prefers-color-scheme: dark) {{
                    :root {{
                        --stat-bg: #2b2b35;
                        --stat-border: #404040;
                        --stat-shadow: 0 1px 3px rgba(0,0,0,0.3);
                        --title-color: #fafafa;
                        --text-color: #fafafa;
                    }}
                }}
                
                /* Streamlit 다크모드 */
                [data-theme="dark"] {{
                    --stat-bg: #2b2b35;
                    --stat-border: #404040;
                    --stat-shadow: 0 1px 3px rgba(0,0,0,0.3);
                    --title-color: #fafafa;
                    --text-color: #fafafa;
                }}
            </style>
        """, unsafe_allow_html=True)

    col1,col2,col3=st.columns(3)

    with col1:
        display_stat("전체 할일",total_todos)
    with col2:
        display_stat("완료된 할일",completed_todos, delta=completed_todos, value_color="#4CAF50")
    with col3:
        display_stat("남은 할일",remaining_tods, delta=-remaining_tods, value_color="#f44336")

    # ------------
    # 21분까지 
    # 할일 추가했는지 먼저 확인
    #     completion_rate 100 일때 모든 할일 완료 custom_success
    #     completion_rate 80 이상일때 거의 다 완료 custom_info
    #     completion_rate 50 이상일때 절반 완료 custom_warning
    #     completion_rate 0 일때 화이팅! custom_error
    if completion_rate==100:
        custom_success("모든 할일 완료")
    elif completion_rate>=80:
        custom_info("거의 다 완료")
    elif completion_rate>=50:
        custom_warning("절반 완료")
    elif completion_rate==0:
        custom_error("화이팅!")
    custom_warning(f"진행률: {completion_rate:.1f}%")
else:
    custom_info("할일을 추가해보세요.")

 

    #     else 진행률 소수점 1자리까지 출력해주세요.
    # 할일 목록이 없으면 할일을 추가해보세요. custom_info








    # ------------

st.divider()

st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.8em;'>
    💡 팁: 엔터키를 눌러서 빠르게 할일을 추가할 수 있어요!
    </div>
    """, 
    unsafe_allow_html=True
)

# st.markdown("""
# <footer style="background-color: #f2f2f2; padding: 20px; text-align: center;">
#   <p>&copy; 2025 나의 웹사이트. 모든 권리 보유.</p>
#   <p>
#     <a href="/about.html">회사 소개</a> | 
#     <a href="/contact.html">문의하기</a> | 
#     <a href="/privacy.html">개인정보 처리방침</a>
#   </p>
# </footer>
# <footer style="background-color: #333; color: white; text-align: center; padding: 20px;">
#     <p>&copy; 2025 Company Name. All rights reserved.</p>
# </footer>
# """, unsafe_allow_html=True)