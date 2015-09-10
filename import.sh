find pkgs  -type f -name '*.json'  | sed 's/.json$//' | while read col; do 
    echo "Importing $col"
    mongoimport -d ckan --jsonArray -c datasets < $col.json;  
done
