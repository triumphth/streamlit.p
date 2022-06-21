{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from gsheetsdb import connect\n",
    "\n",
    "st.title(\"My First Streamlit Web App\")\n",
    "\n",
    "df = pd.DataFrame({\"one\": [1, 2, 3], \"two\": [4, 5, 6], \"three\": [7, 8, 9]})\n",
    "st.write(df)\n",
    "\n",
    "st.title(\"Connect to Google Sheets\")\n",
    "gsheet_url = \"https://docs.google.com/spreadsheets/d/1ixMrhGV1TPn14_oTyEIFjszuwuwO9xkbsc1WEBJH3N0/edit?usp=sharing\"\n",
    "conn = connect()\n",
    "rows = conn.execute(f'SELECT * FROM \"{gsheet_url}\"')\n",
    "df_gsheet = pd.DataFrame(rows)\n",
    "st.write(df_gsheet)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
