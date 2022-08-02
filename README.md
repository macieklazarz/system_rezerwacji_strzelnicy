# Content of project
* [General info](#general-info)
* [Technologies](#technologies)
* [Architecture design](#architecture-design)
* [Setup](#setup)
* [Guideline](#guideline)




## General info
<details>
<summary>Click here to see general information about <b>Project</b>!</summary>
<br>
This app is dedicated to manage shooting range resources. Users can do reservation of particular axes. Basic concept looks as following:
<br>
<ol>
  <li>Admin axes</li>
  <li>User registers account</li>
  <li>User check available axes</li>
  <li>User do reservatin</li>
  <li>(Optional)User/admin deletes reservation</li>
  </ol>
  There are only 2 user types foreseen in the application. User which can manage his own reservations and admin allowed to manage all reservations

</details>

## Technologies
<details>
<summary>Click here to see information about technologies utilized in the <b>Project</b>!</summary>
<br>
Technologies utilized in the frame of this project are:
<br>
<ul>
  <br>
  <li>Django</li>
  <p>Main application localized in container 'web' is based on Django. It allows users to do interaction and it poses as root of whole project.</p>
  <li>Postgres</li>
  <p>PostgreSQL database stores data related to users, axes and reservations.</p>
  <li>Docker</li>
  <p>Docker has been utilized to deploy the app in concept of microservices.</p>
 </ul>
</details>

## Architecture design
<details>
<summary>Click here to see schema related to configuration of the <b>Project</b>!</summary>
<br>
<img src="https://user-images.githubusercontent.com/106651068/182433805-0df64a03-5fea-4b14-8b5b-13f93f939a75.png" width="80%" height="80%"></img>
<br>
</details>

## Setup
<details>
<summary>Click here to see initial steps required to set up application</summary>
<br>
Required action is to download the repository and launch it using Docker.
</details>

## Guideline
<details>
<summary>Click here to see how to use the application</summary>
<br>
Go to main page and click 'Logowanie':
<br>
<img src="https://user-images.githubusercontent.com/106651068/182446906-739444ea-aed9-4b80-afe4-a64f40c2ce53.png" width="50%" height="50%"></img>
<br>
Log in with credentials admin/qapl12!@:
<br>
<img src="https://user-images.githubusercontent.com/106651068/182447094-e70cffe6-c9c4-45ae-aa6b-f37413ae4a2d.png" width="50%" height="50%"></img>
<br>
Now we will add new axis:
<br>
<img src="https://user-images.githubusercontent.com/106651068/182448505-a91ee88e-7e98-4581-a21e-63cbcc017153.png" width="50%" height="50%"></img>
<br>
Fill the form with axis name and description:
<br>
<img src="https://user-images.githubusercontent.com/106651068/182448814-e9e91238-69dd-4a15-8eee-ab85846c748a.png" width="50%" height="50%"></img>
<br>
The axis has been added. Now log out:
<br>
<img src="https://user-images.githubusercontent.com/106651068/182449003-2776d948-7f53-42ca-b173-2806f7e3caec.png" width="50%" height="50%"></img>
<br>
Register new account to add reservation:
<br>
<img src="https://user-images.githubusercontent.com/106651068/182449171-cd97dae9-67df-4f8d-81cc-7449fc403982.png" width="50%" height="50%"></img>
<br>
Fill the form:
<br>
<img src="https://user-images.githubusercontent.com/106651068/182449586-7d59c7b0-482c-4f65-b63f-3c3e6789abb2.png" width="50%" height="50%"></img>
<br>

</details>
