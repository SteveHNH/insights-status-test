FROM nginx
MAINTAINER Stephen Adams <sadams@redhat.com>
RUN apt-get update -y && apt-get upgrade -y && apt-get install jq curl -y && apt-get clean
CMD ["nginx", "-g", "daemon off;"]
