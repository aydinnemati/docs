# File storage, block storage and object storage
see [redhat](https://www.redhat.com/en/topics/data-storage/file-block-object-storage) for more ...

> Files, blocks, and objects are storage formats that hold, organize, and present data in different ways—each with their own capabilities and limitations. File storage organizes and represents data as a hierarchy of files in folders; block storage chunks data into arbitrarily organized, evenly sized volumes; and object storage manages data and links it to associated metadata.

# What is file storage?

> File storage, also called file-level or file-based storage, is exactly what you think it might be: Data is stored as a single piece of information inside a folder, just like you’d organize pieces of paper inside a manila folder. When you need to access that piece of data, your computer needs to know the path to find it. (Beware—It can be a long, winding path.) Data stored in files is organized and retrieved using a limited amount of metadata that tells the computer exactly where the file itself is kept. It’s like a library card catalog for data files.

> Think of a closet full of file cabinets. Every document is arranged in some type of logical hierarchy—by cabinet, by drawer, by folder, then by piece of paper. This is where the term hierarchical storage comes from, and this is file storage. It is the oldest and most widely used data storage system for direct and network-attached storage systems, and it’s one that you’ve probably been using for decades. Any time you access documents saved in files on your personal computer, you use file storage. File storage has broad capabilities and can store just about anything. It’s great for storing an array of complex files and is fairly fast for users to navigate.

> The problem is, just like with your filing cabinet, that virtual drawer can only open so far. File-based storage systems must scale out by adding more systems, rather than scale up by adding more capacity.

# What is block storage?

> Block storage chops data into blocks—get it?—and stores them as separate pieces. Each block of data is given a unique identifier, which allows a storage system to place the smaller pieces of data wherever is most convenient. That means that some data can be stored in a Linux® environment and some can be stored in a Windows unit.

> Block storage is often configured to decouple the data from the user’s environment and spread it across multiple environments that can better serve the data. And then, when data is requested, the underlying storage software reassembles the blocks of data from these environments and presents them back to the user. It is usually deployed in storage-area network (SAN) environments and must be tied to a functioning server.

> Because block storage doesn’t rely on a single path to data—like file storage does—it can be retrieved quickly. Each block lives on its own and can be partitioned so it can be accessed in a different operating system, which gives the user complete freedom to configure their data. It’s an efficient and reliable way to store data and is easy to use and manage. It works well with enterprises performing big transactions and those that deploy huge databases, meaning the more data you need to store, the better off you’ll be with block storage.

> There are some downsides, though. Block storage can be expensive. It has limited capability to handle metadata, which means it needs to be dealt with in the application or database level—adding another thing for a developer or systems administrator to worry about.

# What is object storage?
> Object storage, also known as object-based storage, is a flat structure in which files are broken into pieces and spread out among hardware. In object storage, the data is broken into discrete units called objects and is kept in a single repository, instead of beingkept

> as files in folders or as blocks on servers.

> Object storage volumes work as modular units: each is a self-contained repository that owns the data, a unique identifier that allows the object to be found over a distributed system, and the metadata that describes the data. That metadata is important and includes details like age, privacies/securities, and access contingencies. Object storage metadata can also be extremely detailed, and is capable of storing information on where a video was shot, what camera was used, and what actors are featured in each frame. To retrieve the data, the storage operating system uses the metadata and identifiers, which distributes the load better and lets administrators apply policies that perform more robust searches.

> Object storage requires a simple HTTP application programming interface (API), which is used by most clients in all languages. Object storage is cost efficient: you only pay for what you use. It can scale easily, making it a great choice for public cloud storage. It’s a storage system well suited for static data, and its agility and flat nature means it can scale to extremely large quantities of data. The objects have enough information for an application to find the data quickly and are good at storing unstructured data.

> There are drawbacks, to be sure. Objects can’t be modified—you have to write the object completely at once. Object storage also doesn’t work well with traditional databases, because writing objects is a slow process and writing an app to use an object storage API isn’t as simple as using file storage.

# Object Storage vs. File Storage vs. Block Storage
## Object storage
- takes each piece of data and designates it as an object. Data is kept in separate storehouses versus files in folders and is bundled with associated metadata and a unique identifier to form a storage pool.

## File storage
- stores data as a single piece of information in a folder to help organize it among other data. This is also called hierarchical storage, imitating the way that paper files are stored. When you need access to data, your computer system needs to know the path to find it.

## Block storage
- takes a file apart into singular blocks of data and then stores these blocks as separate pieces of data. Each piece of data has a different address, so they don't need to be stored in a file structure.

# Object Storage
- shared access to data
- heterogenous computing(Heterogeneous computing refers to systems that use more than one kind of processor or cores)
- dynamic scaling without interruption
- __client is app(api)__ => good access, security, etc
- easy to change platforms (windows, linux, mobile platforms, etc)
- consistency
- dont have permission problems
- no fragmentations
- easy to scale and unlimited to scaling
- metadata for additional information for searching and get better resaults
- security is so important
- super high performance
- Data durability
- Data availability

## what is it?
>-  object storage(object-base storage) is a strategy that manages and manipulates data in distinc units, called onject.
> - these objects are kept in a single storehouse and not related to other files or folders insted, object storage combines the pices of data that makes a file and adds all its meta data to it and attaches a identifire.
> - it not have any levels and keep everything in a flat address space called a storage pool.
> - This metadata is key to the success of object storage in that it provides deep analysis of the use and function of data in the storage pool

## Benefits of Object Storage

> Now that we've described what object storage is, what are its benefits?

- Greater data analytics. Object storage is driven by metadata, and with this level of classification for every piece of data, the opportunity for analysis is far greater.
- Infinite scalability. Keep adding data, forever. There's no limit.
- Faster data retrieval. Due to the categorization structure of object storage, and the lack of folder hierarchy, you can retrieve your data much faster.
- Reduction in cost. Due to the scale-out nature of object storage, it's less costly to store all your data.
- Optimization of resources. Because object storage does not have a filing hierarchy, and the metadata is completely customizable, there are far fewer limitations than with file or block storage.

## a new model for 

## What is Amazon S3 Storage?
> - Amazon Simple Storage Service (S3) is a storage system for the internet, where you can store and retrieve any amount of data, anytime, anywhere. This make web-scaling computing easier for developers, and it also gives them access to the infrastructure that Amazon uses to conduct a global network of websites. The Amazon S3 API offers a common path for rapid development and the creation of hybrid cloud deployments at scale. 

# Block Storage
- fast
- good random access
- low latency
- not intelegent
- client via OS


# ceph and object storage 
- use librados in your app to power up performance with using ceph's native protocols to communicate with cluster. Librados is available for several languages, including C, C++, Python, PHP, and Java.
