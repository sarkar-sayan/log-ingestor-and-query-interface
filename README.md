<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Log Ingestor and Query Interface</h3>

  <p align="center">
    Develop a log ingestor system that can efficiently handle vast volumes of log data, and offer a simple interface for querying this data using full-text search or specific field filters. Both the systems (the log ingestor and the query interface) can be built using any programming language of your choice. The logs should be ingested (in the log ingestor) over HTTP, on port `3000`.
    <br />
    <a href="https://github.com/dyte-submissions/november-2023-hiring-sarkar-sayan"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dyte-submissions/november-2023-hiring-sarkar-sayan">View Demo</a>
    ·
    <a href="https://github.com/dyte-submissions/november-2023-hiring-sarkar-sayan/issues">Report Bug</a>
    ·
    <a href="https://github.com/dyte-submissions/november-2023-hiring-sarkar-sayan/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">System Design</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started/ README</a>
    </li>
    <li><a href="#roadmap">Identified Issues</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Sample Log Data Format:

The logs to be ingested will be sent in this format.

```json
{
	"level": "error",
	"message": "Failed to connect to DB",
  "resourceId": "server-1234",
	"timestamp": "2023-09-15T08:00:00Z",
	"traceId": "abc-xyz-123",
  "spanId": "span-456",
  "commit": "5e5342f",
  "metadata": {
      "parentResourceId": "server-0987"
    }
}
```

## Requirements

The requirements for the log ingestor and the query interface are specified below.

### Log Ingestor:

- Develop a mechanism to ingest logs in the provided format.
- Ensure scalability to handle high volumes of logs efficiently.
- Mitigate potential bottlenecks such as I/O operations, database write speeds, etc.
- Make sure that the logs are ingested via an HTTP server, which runs on port `3000` by default.

### Query Interface:

- Offer a user interface (Web UI or CLI) for full-text search across logs.
- Include filters based on:
    - level
    - message
    - resourceId
    - timestamp
    - traceId
    - spanId
    - commit
    - metadata.parentResourceId
- Aim for efficient and quick search results.

## Advanced Features (Bonus):

These features aren’t compulsory to implement, however, adding them might increase the chances of your submission being accepted.

- Implement search within specific date ranges.
- Utilize regular expressions for search.
- Allow combining multiple filters.
- Provide real-time log ingestion and searching capabilities.
- Implement role-based access to the query interface.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### System Design

#### Log Ingestor
The Log Ingestor uses Flask as an HTTP server for log ingestion. It stores logs in SQLite for structured data and Elasticsearch for efficient search capabilities.

#### Query Interface
The Query Interface is a command-line interface (CLI) built with Click. It allows users to perform searches and apply filters on logs stored by the Log Ingestor.

#### Features Implemented
Log Ingestor:

- Ingests logs over HTTP on port 3000.
- Stores logs in both SQLite and Elasticsearch for scalability.
  
Query Interface:

- CLI for user interaction.
- Search logs based on various parameters (level, message, resourceId, etc.).
- Additional features: Date range search, regular expression search, and combined filters.
  
Advanced Features (Bonus):

- Date range search in Query Interface.
- Regular expression search in Query Interface.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started/ README

# Log Ingestor and Query Interface

This project consists of a Log Ingestor and a Query Interface. The Log Ingestor ingests logs over HTTP and stores them, while the Query Interface allows users to search and filter logs.

## Running the Project

### Log Ingestor

1. Install the necessary dependencies:

   ```bash
   pip install flask
   pip install sqlite3
   pip install elasticsearch
2. Run the Log Ingestor:

    ```bash
    python log_ingestor.py
The Log Ingestor will run on http://localhost:3000 by default.

### Query Interface

1. Install the necessary dependencies:

   ```bash
   pip install click
2. Run the Query Interface:

    ```bash
    python query_interface_cli.py query_logs

This will display options for filtering logs. Use the available options to query logs.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Identified Issues

### Limited Error Handling:

-The error handling in both Log Ingestor and Query Interface is basic. Further refinement is needed.
### Security Considerations:

- This example doesn't cover security aspects. In a production environment, consider securing the API endpoints and implementing authentication.
### Real-time Ingestion and Searching:

- The implementation lacks real-time log ingestion and instant searching. This could be achieved with additional tools or frameworks.
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@linkedin_profile](https://www.linkedin.com/in/sayan-sarkar-960302252/) - sayansarkar.careers@gmail.com

Project Link: [https://github.com/dyte-submissions/november-2023-hiring-sarkar-sayan](https://github.com/dyte-submissions/november-2023-hiring-sarkar-sayan)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
