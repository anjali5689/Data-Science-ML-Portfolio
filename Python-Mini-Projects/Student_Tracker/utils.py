import streamlit as st
from functools import wraps

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st.write(f"➡️ Calling `{func.__name__}()`")
        result = func(*args, **kwargs)
        st.write(f"⬅️ Exiting `{func.__name__}()`")
        return result
    return wrapper
