import pandas as pd
import streamlit as st

class DataImport:
    """"
    Import data from CSV file on Google Cloud
    """
    def __init__(self):
        pass

    @st.cache_data(ttl=60*60) # ttl of one hour to keep memory in cache
    def fetch_and_clean_data(_arg):
        data_url = 'job_postings.csv'
        df = pd.read_csv(data_url)
        df = df.drop(labels=['Unnamed: 0'], axis=1, errors='ignore')
        # df.Job_Skills = df.Job_Skills.str.strip("[]").str.split(",") # fix major formatting issues with tokens
        # df.Job_Skills = df.Job_Skills.apply(lambda row: [x.strip(" ") for x in row]) # remove whitespace from tokens
        # Converting Job Posting Date to datetime format
        # df['date_time'] = pd.to_datetime(df['date_time'])

        # Replacing "power_bi" with "powerbi"
        df['Job_Skills'] = df['Job_Skills'].str.replace('sql', 'SQL')
        df['Job_Skills'] = df['Job_Skills'].str.replace('t-sql', 'SQL')
        df['Job_Skills'] = df['Job_Skills'].str.replace('t-SQL', 'SQL')
        df['Job_Skills'] = df['Job_Skills'].str.replace('mySQL', 'SQL')

        df['Job_Skills'] = df['Job_Skills'].str.replace('python', 'Python')
        df['Job_Skills'] = df['Job_Skills'].str.replace('pyspark', 'SPARK')
        df['Job_Skills'] = df['Job_Skills'].str.replace('spark', 'SPARK')

        df['Job_Skills'] = df['Job_Skills'].str.replace('sas' , 'SAS')
        # df['Job_Skills'] = df['Job_Skills'].str.replace('saas', 'SAS')
        df['Job_Skills'] = df['Job_Skills'].str.replace('sSAS', 'SAS')
        df['Job_Skills'] = df['Job_Skills'].str.replace('SASs', 'SAS')

        df['Job_Skills'] = df['Job_Skills'].str.replace('tensorflow', 'TensorFlow')
        df['Job_Skills'] = df['Job_Skills'].str.replace('hadoop', 'Hadoop')
        df['Job_Skills'] = df['Job_Skills'].str.replace('azure', 'Azure')
        # df['Job_Skills'] = df['Job_Skills'].str.replace('go', 'Go')
        df['Job_Skills'] = df['Job_Skills'].str.replace('devops', 'Devops')
        df['Job_Skills'] = df['Job_Skills'].str.replace('jquery', 'JQuery')
        df['Job_Skills'] = df['Job_Skills'].str.replace('kotlin', 'Kotlin')

        df['Job_Skills'] = df['Job_Skills'].str.replace('manGo', 'MongoDB')
        df['Job_Skills'] = df['Job_Skills'].str.replace('monGodb', 'MongoDB')
        df['Job_Skills'] = df['Job_Skills'].str.replace('data_lake' , 'Database')
        df['Job_Skills'] = df['Job_Skills'].str.replace('data_lakes' , 'Database')
        df['Job_Skills'] = df['Job_Skills'].str.replace('databases', 'Database')
        df['Job_Skills'] = df['Job_Skills'].str.replace('Databases', 'Database')

        df['Job_Skills'] = df['Job_Skills'].str.replace('docker', 'Docker')
        df['Job_Skills'] = df['Job_Skills'].str.replace('rust', 'Rust')
        df['Job_Skills'] = df['Job_Skills'].str.replace('node.js' , 'NodeJS')
        df['Job_Skills'] = df['Job_Skills'].str.replace('vue', 'VueJS')
        df['Job_Skills'] = df['Job_Skills'].str.replace('codebase', 'SPARK')
        df['Job_Skills'] = df['Job_Skills'].str.replace('oracle' , 'Oracle')
        df['Job_Skills'] = df['Job_Skills'].str.replace('excel' , 'Excel')
        df['Job_Skills'] = df['Job_Skills'].str.replace('database' , 'Database')
        df['Job_Skills'] = df['Job_Skills'].str.replace('jupyter', 'Jupyter Notebook')
        df['Job_Skills'] = df['Job_Skills'].str.replace('go ' , 'Go')
        df['Job_Skills'] = df['Job_Skills'].str.replace('aws' , 'AWS')
        df['Job_Skills'] = df['Job_Skills'].str.replace('java' , 'Java')
        df['Job_Skills'] = df['Job_Skills'].str.replace('ruby', 'Ruby')
        df['Job_Skills'] = df['Job_Skills'].str.replace('github', 'Github')
        df['Job_Skills'] = df['Job_Skills'].str.replace('css', 'Fullstack')
        df['Job_Skills'] = df['Job_Skills'].str.replace('programming', 'OOPS concept')
        df['Job_Skills'] = df['Job_Skills'].str.replace('coding', 'OOPS concept')
        df['Job_Skills'] = df['Job_Skills'].str.replace('codebase', 'OOPS concept')
        df['Job_Skills'] = df['Job_Skills'].str.replace('PowerBitbucket', 'PowerBi')

        df['Job_Skills'] = df['Job_Skills'].str.replace('power_bi', 'PowerBi')
        df['Job_Skills'] = df['Job_Skills'].str.replace('powerbi', 'PowerBi')
        df['Job_Skills'] = df['Job_Skills'].str.replace('tableau', 'Tableau')

        df['Job_Skills'] = df['Job_Skills'].str.replace('ml', 'Machine Learning')
        df['Job_Skills'] = df['Job_Skills'].str.replace('xMachine Learning', 'Machine Learning')
        df['Job_Skills'] = df['Job_Skills'].str.replace('Machine Learningops', 'Machine Learning')

        df['Job_Skills'] = df['Job_Skills'].str.replace('machine_learning', 'Machine Learning')
        df['Job_Skills'] = df['Job_Skills'].str.replace('Machine Learning5', 'Machine Learning')
        df['Job_Skills'] = df['Job_Skills'].str.replace('htMachine Learning', 'Machine Learning')
        df['Job_Skills'] = df['Job_Skills'].str.replace('back-end', 'Backend')
        df['Job_Skills'] = df['Job_Skills'].str.replace('backend', 'Backend')

        df['Job_Skills'] = df['Job_Skills'].str.replace('agile', 'Agile')
        df['Job_Skills'] = df['Job_Skills'].str.replace('scrum', 'Agile')
        df['Job_Skills'] = df['Job_Skills'].str.replace('postgreSQL', 'PostgreSQL')

        df['Job_Skills'] = df['Job_Skills'].str.replace('postgres', 'PostgreSQL')
        df['Job_Skills'] = df['Job_Skills'].str.replace('linux', 'Linux')
        df['Job_Skills'] = df['Job_Skills'].str.replace('unix', 'Linux')
        # df['Job_Skills'] = df['Job_Skills'].str.replace('unix/linux', 'Linux')
        df['Job_Skills'] = df['Job_Skills'].str.replace('ubuntu', 'Linux')
        df['Job_Skills'] = df['Job_Skills'].str.replace('javascript/typescript', 'Javascript')
        df['Job_Skills'] = df['Job_Skills'].str.replace('Javascriton', 'Javascript')
        df['Job_Skills'] = df['Job_Skills'].str.replace('powerpoints', 'Powerpoint')
        df['Job_Skills'] = df['Job_Skills'].str.replace('spreadsheets', 'Spreadsheet')
        df['Job_Skills'] = df['Job_Skills'].str.replace('no-sql', 'NoSQL')
        df['Job_Skills'] = df['Job_Skills'].str.replace('no-SQL', 'NoSQL')
        df['Job_Skills'] = df['Job_Skills'].str.replace('noSQL', 'NoSQL')
        df['Job_Skills'] = df['Job_Skills'].str.replace('msSQL', 'MySQL')
        df['Job_Skills'] = df['Job_Skills'].str.replace('noSQL', 'NoSQL')

        df['Job_Skills'] = df['Job_Skills'].str.replace('frontend', 'Fullstack')
        df['Job_Skills'] = df['Job_Skills'].str.replace('fullstack', 'Fullstack')
        df['Job_Skills'] = df['Job_Skills'].str.replace('back-end', 'Backend')

        df['Job_Skills'] = df['Job_Skills'].str.replace('node', 'NodeJS')
        df['Job_Skills'] = df['Job_Skills'].str.replace('pl/sql', 'SQL')
        df['Job_Skills'] = df['Job_Skills'].str.replace('pl/SQL', 'SQL')

        return df