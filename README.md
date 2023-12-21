# Resume Parser using OPENAI GPT

This project is developed as part of a POC done for learning purpose. This project is intended to parse the given resume and generate a json file with the parsed data.

### Instructions to setup the project

<ol>
    <li>First we need to have openai api key. This can be generated from openai web site.</li>
    <li>Next step it to update the key in environment.</li>
    <ol>
        <li>Open .env file.</li>
        <li>Replace <code>"YOUR API KEY"</code> with your api key.</li>
    </ol>
    <li>Download all the python dependencies by running command <code>pip install -r requirements.txt</code>.</li>
</ol>

### Instructions to run the project and parse the given resume

<ol>
    <li>Replace <code>sample-resume.pdf</code> file with your resume.</li>
    <li>Delete file <code>parsed_resume.json</code>.</li>
    <li>Run command <code>python3 resumeParser.py</code></li>
</ol>

The sample_resume.pdf file will get parsed and a new parsed_resume.json file will get generated with parsed details.