db = db.getSiblingDB("instagramdb");

db.createCollection("users");
db.createCollection("posts");
db.createCollection("comments");
db.createCollection("likes");
db.createCollection("notifications");

