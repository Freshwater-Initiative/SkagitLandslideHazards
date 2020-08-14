# SkagitLandslideHazards
Seattle City Light is interested in improving understanding of landslide hazard and sediment transport to ensure reliable and cost-effective hydropower generation.

## Quicklinks to HydroShare Resources:
To access and download Seattle City Light Contract Deliverables [Landslide Hazard Modeling in the Skagit Basin](https://www.hydroshare.org/resource/70d746c7da584ae6bd2f88deb5a4c188/)
contains the working folder of data and code and all GIS files.

To interact with the data and code online, the resource contains files used to run the model 
[Slippery Future Data: Predicting future regional landslide probability using soil saturation](https://www.hydroshare.org/resource/01b486f301864828ba2cd9ab7ac77c4e/).  This this is the resource we use Launch Notebooks and code: [Slippery Future Code: Predicting future regional landslide probability using soil saturation](https://www.hydroshare.org/resource/4cac25933f6448409cab97b293129b4f/)


## Read more about the project:
Landslide probability modeling can be used to better understand landslides in the watersheds containing the electrical transmission lines and facilities. A recently published landslide model (Strauch et al. 2018) updated to use spatially distributed saturation (depth to water table) derived from a basin calibrated hydrologic model (Distributed Hydrology Soil and Vegetation Model - DHSVM) at 150-m grid resolution. Contemporary and future probability of landslide initiation is used to create landslide hazard maps at a 30-m resolution. Our case study of the Skagit Hydroelectric Project evaluates the sensitivity of the landslide model to subsurface saturation and reduced cohesion of a simulated a fire. We compare historic landslide probability to two future time periods using two scenarios (RCP 4.5 and RCP 8.5) and a representative distribution of global climate models (GCMs).

This resource is an updated copy of the work published in Strauch et al., (2018) "A hydroclimatological approach to predicting regional landslide probability using Landlab", Earth Surf. Dynam., 6, 1-26 . It demonstrates a hydroclimatological approach to modeling of regional shallow landslide initiation based on the infinite slope stability model coupled with a steady-state subsurface flow representation. The model component is available as the LandslideProbability component in Landlab, an open-source, Python-based landscape earth systems modeling environment described in Hobley et al. (2017, Earth Surf. Dynam., 5, 21–46, https://doi.org/10.5194/esurf-5-21-2017). 

## Technical Steps to Get Started Developing Content and Code from the repository

## Notebook User Instructions for interactive compute 

#### If you are new to this cyber-ecosystem, start at Section 1.0. As you learn, start your work at other sections.

### 1.0 Get access to the data
Go to HydroShare.org and login at www.hydroshare.org. You will need a HydroShare user account to download data from the HydroShare data repository.  We also use this user ID to access computational resources and servers. 

VOCAB: Server: it could be high performance or under your friends desk.  It's an online networked computer that enables you to access it from your web browser. 

### 2.0 Get access to a computer

#### Notebook User Instructions specific for interactive compute on [CyberGIS for Water](https://www.hydroshare.org/group/157)

2.1 **Do one time** From the HydroShare website, top dashboard, Go to Collaborate. Find the CyberGIS for Water Compute Group, Ask to Join. An owner of a compute group may also invite you to join using your email or HydroShare User ID.  An owner must confirm membership in order to access their server from a HydroShare resource.

2.2. **Next time** Go directly to https://js-168-155.jetstream-cloud.org/

- Example link to the File Directory View: https://js-168-155.jetstream-cloud.org/user/christinabandaragoda/tree
- Example link to the Jupyter Lab View: https://js-168-155.jetstream-cloud.org/user/christinabandaragoda/lab

New users: Get familiar with JupyterHub platform with [Juptyer Notebook new user instructions](   ) and [JuptyerHub Documentation](https://jupyterhub.readthedocs.io/en/stable/index.html)

2.3. Open a Jupyter Notebook.  The example is enabled with code to interact with this repository.  

Open a New Notebook  `Untitled.ipynb`.  Save, rename, navigate the folder structure.  

### 3.0 Setup to Push/Pull code using Github
3.1 **Do one time** Use Jupyter Lab interface to add a Github folder to your user space and clone this repository. 
Add a new Folder using the + icon. Name it Github. 
Open a terminal. 
`cd /home/jovyan/work`
`pwd`
`ls`
`cd /home/jovyan/work/Github`
```
> git clone https://github.com/Freshwater-Initiative/SkagitLandslideHazards.git

```

3.2 **Do one time**  Use a new "Terminal" session and clone the github repository by running the command:

The terminal opens in /home/jovyan/

```
> cd data

```
Make a new directory specific to your Github repositories on this server. 

```
> mkdir Github   

```
Clone the github repository by running the command:

```
> git clone https://github.com/Freshwater-Initiative/SkagitLandslideHazards.git

```
Open a Notebook using the directory structure on the left, go to Notebooks folder, click on a Notebook.ipynb

### 4.0 Pull code using Github

If this repository changes, and you do not have any changes to save, simply pull the changes to your workspace.
Go back to the terminal view and run these lines.

```
> cd SkagitLandslideHazards
> git pull
```
Open a Notebook using the directory structure on the left, go to Notebooks folder, click on the changed Notebook.ipynb

### 5.0 Push code using Github
5.1 **Do one time** Set up permissions with Github from this computer

Run
```
  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"
```
to set your account's default identity.
Omit --global to set the identity only in this repository.
```
git config --global user.email "myemail@univ.edu
git config --global user.name "ChristinaB"
```
Do some work in a Notebook. Then use this sequence to tell Github that all changed files should be staged to move from the server to Github. Status prints out the changes, so you always review what you are going to push before you push it. Commiting the change with a message is the same task as uploading a file or changing a file from github.com repository interface.  
```
git add *
git status
git commit -m"this is a brief useful note on the change or work"
git push
```
### Notebook User Instructions for interactive compute on [CSDMS JupyterHub](https://www)
Work in Progress.



**Earlier publications on HydroShare:**

Strauch, R., E. Istanbulluoglu, S. S. Nudurupati, C. Bandaragoda (2018). Regional landslide hazard using Landlab - NOCA Observatory, HydroShare, http://www.hydroshare.org/resource/3a925bd4a5784a38944b1e8b51224de1

Strauch, R., E. Istanbulluoglu, S. S. Nudurupati, C. Bandaragoda (2017). Regional landslide hazard using Landlab - NOCA Data, HydroShare, https://doi.org/10.4211/hs.a5b52c0e1493401a815f4e77b09d352b
