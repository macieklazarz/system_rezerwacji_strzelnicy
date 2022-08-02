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
Get secret key from keycloak:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172534035-a551137a-c5e9-45fb-8ecb-f3a6aa7462a8.png" width="50%" height="50%"></img>
<br>
Enter using credentials admin/password:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172534442-4a397872-ffc0-4a17-97a0-224f708dfe65.png" width="80%" height="80%"></img>
<br>
Go to Clients section and click on admin-cli:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172848374-d63935b3-b817-40c1-be24-ec645bc02130.png" width="80%" height="80%"></img>
<br>
In credentials section click Regenerate Secret and copy the code:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172848647-2ad3ecdb-ae62-4b75-93cb-10bf505c478a.png" width="80%" height="80%"></img>
<br>
Paste it into proper place in .env file and restart containers:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172848892-bc374d9a-a537-4e07-ac54-f4c55d669a4a.png" width="80%" height="80%"></img>
<br>
Add user with credentials admin/password:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172534861-5add6c26-05ff-4bbc-84ec-5ee59f306630.png" width="80%" height="80%"></img>
<br>
<img src="https://user-images.githubusercontent.com/106651068/172534975-6fe5ada5-95f3-4a35-8438-a135bd9773ad.png" width="80%" height="80%"></img>
<br>
<img src="https://user-images.githubusercontent.com/106651068/172535039-329b64fa-99de-43cc-82dd-75460fce9d62.png" width="80%" height="80%"></img>
<br>
Assign manage-user role:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172911147-5eb0da64-56bf-44ac-94f2-ce7008a054c5.png" width="80%" height="80%"></img>
<br>
Make sure that your configuration looks as following:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172535122-ee6c8623-6f90-4338-bc0b-0e964c7dbedb.png" width="80%" height="80%"></img>
<br>
Now it is time to create users. We will create admin user responsible for adding competitions and challanges, referee user responsible for editing results 
and basic user allowed to enroll to challanges. Lets enter to initial competition and  start with creating admin user:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172536041-54fb2d75-178f-4133-be9e-cf5e703225e4.png" width="80%" height="80%"></img>
<br>
Go to register section and fill the form:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172536180-9fcae087-4853-47a3-ae52-7e61365cbabc.png" width="80%" height="80%"></img>
<br>
We need to assign created user to admin role. Come back to keycloak, click on users section on left side and click hiperlink related to created user:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172536671-6f0064b4-948c-4084-ae0d-3c583876038b.png" width="80%" height="80%"></img>
<br>
Take role admin to assigned roles:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172536964-6956e0f4-5746-41f9-9369-1bca5b06617b.png" width="80%" height="80%"></img>
<br>
Create referee user:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172836435-1588f0db-724c-4e23-89f3-72fc6ab57928.png" width="80%" height="80%"></img>
<br>
We need to assign created user to referee role. Come back to keycloak and click hiperlink related to created user:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172838981-cb0a663b-8d81-411d-9a25-1e8f575da943.png" width="80%" height="80%"></img>
<br>
Take role referee to assigned roles:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172836793-4a4395ad-38db-4b43-80ba-82cb39bf0fd2.png" width="80%" height="80%"></img>
<br>
Go to register section once again and register new basic user:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172541485-484ecd1c-670a-45ef-a3a9-96a3b1175cd1.png" width="80%" height="80%"></img>
<br>
All types of users have been added. Now log into app as admin:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172537259-0b8b3343-db8a-43cd-9d3e-ef0ea246614d.png" width="80%" height="80%"></img>
<br>
Create new competition:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172537363-c5f180e6-4e6b-4d18-b721-0a50bdbd15c5.png" width="80%" height="80%"></img>
<br>
<img src="https://user-images.githubusercontent.com/106651068/172537506-4ff56cc3-ac09-4b0c-ad10-41961093efde.png" width="80%" height="80%"></img>
<br>
Create new challange assigned to newly created competition:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172837568-36497db9-16c1-4a59-8c3e-759fb7c133a4.png" width="80%" height="80%"></img>
<br>
Competition and challange have been added. Log out, come back to main page (localhost:5000) and get into newly created competition:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172830327-9e34cfc4-3a06-46a5-8770-7801c958a24a.png" width="80%" height="80%"></img>
<br>
Log in as basic user:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172843359-1b22a068-5db6-4e45-b319-7bf624cb0e08.png" width="80%" height="80%"></img>
<br>
Enroll to challange:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172542086-a223efc5-f60d-417c-a650-42fa24de91b8.png" width="80%" height="80%"></img>
<br>
Log out and after that log in as a referee:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172837783-3abcfad9-1117-4539-9274-0722eabe32e7.png" width="80%" height="80%"></img>
<br>
Modify result:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172838014-079b403c-b107-40d2-bed6-533f34fd0501.png" width="80%" height="80%"></img>
<br>
<img src="https://user-images.githubusercontent.com/106651068/172838128-174cca4c-c06e-477d-aaa6-a1910ec5d48a.png" width="50%" height="50%"></img>
<br>
Log out and log in as basic user:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172843359-1b22a068-5db6-4e45-b319-7bf624cb0e08.png" width="80%" height="80%"></img>
<br>
Check the result:
<br>
<img src="https://user-images.githubusercontent.com/106651068/172843549-306a9e5f-f233-484c-a887-db9b66fda9bc.png" width="80%" height="80%"></img>
</details>
