# import streamlit as st
# from streamlit_gsheets import GSheetsConnection
# import pandas as pd

# # Display Title and Description
# st.title("Vendor Management Portal")
# st.markdown("Enter the details of the new vendor below.")

# # Establishing a Google Sheets connection
# conn = st.experimental_connection("gsheets", type=GSheetsConnection)

# # Fetch existing vendors data
# existing_data = conn.read(worksheet="Vendors", usecols=list(range(6)), ttl=5)
# existing_data = existing_data.dropna(how="all")

# # List of Business Types and Products
# BUSINESS_TYPES = [
#     "Manufacturer",
#     "Distributor",
#     "Wholesaler",
#     "Retailer",
#     "Service Provider",
# ]
# PRODUCTS = [
#     "Electronics",
#     "Apparel",
#     "Groceries",
#     "Software",
#     "Other",
# ]

# # Onboarding New Vendor Form
# with st.form(key="vendor_form"):
#     company_name = st.text_input(label="Company Name*")
#     business_type = st.selectbox("Business Type*", options=BUSINESS_TYPES, index=None)
#     products = st.multiselect("Products Offered", options=PRODUCTS)
#     years_in_business = st.slider("Years in Business", 0, 50, 5)
#     onboarding_date = st.date_input(label="Onboarding Date")
#     additional_info = st.text_area(label="Additional Notes")

#     # Mark mandatory fields
#     st.markdown("**required*")

#     submit_button = st.form_submit_button(label="Submit Vendor Details")

#     # If the submit button is pressed
#     if submit_button:
#         # Check if all mandatory fields are filled
#         if not company_name or not business_type:
#             st.warning("Ensure all mandatory fields are filled.")
#             st.stop()
#         elif existing_data["CompanyName"].str.contains(company_name).any():
#             st.warning("A vendor with this company name already exists.")
#             st.stop()
#         else:
#             # Create a new row of vendor data
#             vendor_data = pd.DataFrame(
#                 [
#                     {
#                         "CompanyName": company_name,
#                         "BusinessType": business_type,
#                         "Products": ", ".join(products),
#                         "YearsInBusiness": years_in_business,
#                         "OnboardingDate": onboarding_date.strftime("%Y-%m-%d"),
#                         "AdditionalInfo": additional_info,
#                     }
#                 ]
#             )

#             # Add the new vendor data to the existing data
#             updated_df = pd.concat([existing_data, vendor_data], ignore_index=True)

#             # Update Google Sheets with the new vendor data
#             conn.update(worksheet="Vendors", data=updated_df)

#             st.success("Vendor details successfully submitted!")



import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("Vendor Management Portal")
st.markdown("Enter the details of the new vendor below.")

# Google Sheets API 키 파일의 내용을 JSON 형식으로 포함
credentials = {
  "type": "service_account",
  "project_id": "my-moral",
  "private_key_id": "d24c05044aa7539de104edf31b29281b57052bcc",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDBGE+t9FCLaP3q\ntD8lFYeM8Di179cHwz8OTbvUr5SeOSyBvq80+VVko/DJsC4t+RcEwn88zi4xUWla\nBP9a0abVk1nLblkEFEgIRqwgLcp8GWzqvSN46zaU4YddMnaAptIQtIlfhXs0LhIQ\nNq68L6I+uLaidSdZTKlcM3PaXT/alAw64ZA8DNext4l7X86ytDrAc5H0Fsd16+3n\npH1WkWN8tcEUnpjq0lsJxirSWCaNdwn4aZadhsaENdX/umPIgwUffKdaHt1CMIZU\nvw7sfZEnE7XRIxmM+xULI2hECquSMEWD4K92VuvZ0Wu9rctA1EVvLEfgpQa57msY\nS8977AHnAgMBAAECggEACFvaDyi1V+Oaok9dMGjHLmWzvsR8JXzhPOhGikVzhInr\nEE7F3OAyPyINqV10Ek9nHLCiu2ode8sPaXMv7qmGtFYlm/XR6qhKGfmdN+NjkY20\nNlEruO9NtJIyvukRUi5mh4yZKcZod/DKnWMQm1rghiCO32d85ZO4/SHJERnaSsbs\nnptEmBkkLfe1MI+rOl+t9qb8/O5AtE43RSjgcmZLVb2kRji4STbRiJYnlt/590/V\npao9IM4BiBJCtvFVY11NAvabhHVcuhac5RN8dAOXoVfCUPoLuq00zehwZuIVujaV\nTtU7sbIxwElzCOMyGwtJWh8vgoClHLwdy60vpl1q+QKBgQDpwOU2uqPmq9WSm/UL\nomeVVR4e3PKA9IH8OvaxvYB9Q/EYqJyz58rZh5GNToemvxsZ9e9gwh4zmfrXxnAQ\n8a0BRzHfyP1sHbNb+NVDk1+UJHA0XPFUxEbx59HVGcCcyZAYcgsg7/qoDY7l9Hj+\nXcQLegp9szL0ivvG+Pu7RQi2DQKBgQDTeNKkdW6xCSQu+bBDSRD4OeODhUxfinHV\nN1vOXsv7msRLq+UnV2QFTp5bMEuBZ4IFWb79L1Dm097hmb+ZysW9E25hJJZfDf1N\nZhNYbq3ydWJLsmy4LQ1WYb14J88Z2xiYJHbZ9/pReGmQ2sgQ/l6bGuR2YFMnoBVV\ni5kM8h8uwwKBgGDjDx6sJZtKxe9KrTrxSbXf3eg09F72+ZmuZuos/cDuFFSALtNy\n0+VuB6pmTluTAoy0H1AfpZ0Fya7+FR0wzuCkvctf54qUlO8eKGcmAovIvqk1jOHx\nqOZDi/mj/u39rbg0LOCuF1roo740oqHsA4IuR4Lqb8hkgw9pzA1HA+FRAoGBAK9T\nadid3/L5MD2eF8wBRQd3/y/okSRZBP2QUxYrNBVbAEn4rxlJ9AwOXW4fAUq9RWgo\nOxdwZjOqDwydyuO34O9cr9PsYJtYXt0PtxRHVwJA3gkCWe7sszUd/dcjsimuo5po\nCP24AZoQKf3F1b95FXik+CtIu0iMCYQOJAs+pim/AoGAGzguD5jA0q09pfHPDPnl\nyiKlefTSzFVYbFsvta8vbzwhmq0ZapJTEru0P/wTNlyGuoENm47zzRPW3TuJO/LM\nbWkyiyFuNtALcNhvKqmsGvpyTlFwKuSXQEiQsc+h6GaPB6MIDAEF6e3hsae3p2zk\npvb0+LioP9XtGewbzbzlEVY=\n-----END PRIVATE KEY-----\n",
  "client_email": "gsheets-python-access@my-moral.iam.gserviceaccount.com",
  "client_id": "101509454515684235283",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/gsheets-python-access%40my-moral.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}


# Establishing a Google Sheets connection
conn = GSheetsConnection(credentials)

# Fetch existing vendors data
existing_data = conn.read(spreadsheet="your-spreadsheet-id", worksheet="Vendors", usecols=list(range(6)), ttl=5)
existing_data = existing_data.dropna(how="all")

# List of Business Types and Products
BUSINESS_TYPES = [
    "Manufacturer",
    "Distributor",
    "Wholesaler",
    "Retailer",
    "Service Provider",
]
PRODUCTS = [
    "Electronics",
    "Apparel",
    "Groceries",
    "Software",
    "Other",
]

# Onboarding New Vendor Form
with st.form(key="vendor_form"):
    company_name = st.text_input(label="Company Name*")
    business_type = st.selectbox("Business Type*", options=BUSINESS_TYPES, index=None)
    products = st.multiselect("Products Offered", options=PRODUCTS)
    years_in_business = st.slider("Years in Business", 0, 50, 5)
    onboarding_date = st.date_input(label="Onboarding Date")
    additional_info = st.text_area(label="Additional Notes")

    # Mark mandatory fields
    st.markdown("**required*")

    submit_button = st.form_submit_button(label="Submit Vendor Details")

    # If the submit button is pressed
    if submit_button:
        # Check if all mandatory fields are filled
        if not company_name or not business_type:
            st.warning("Ensure all mandatory fields are filled.")
            st.stop()
        elif existing_data["CompanyName"].str.contains(company_name).any():
            st.warning("A vendor with this company name already exists.")
            st.stop()
        else:
            # Create a new row of vendor data
            vendor_data = pd.DataFrame(
                [
                    {
                        "CompanyName": company_name,
                        "BusinessType": business_type,
                        "Products": ", ".join(products),
                        "YearsInBusiness": years_in_business,
                        "OnboardingDate": onboarding_date.strftime("%Y-%m-%d"),
                        "AdditionalInfo": additional_info,
                    }
                ]
            )

            # Add the new vendor data to the existing data
            updated_df = pd.concat([existing_data, vendor_data], ignore_index=True)

            # Update Google Sheets with the new vendor data
            conn.update(spreadsheet="your-spreadsheet-id", worksheet="Vendors", data=updated_df)

            st.success("Vendor details successfully submitted!")

