1. 在dockerHub上取得[gitLab](https://hub.docker.com/_/gitlab-community-edition)的image。
2. 运行docker
    1. (__方法1__) 直接运行Image
        ```bash
        # $GITLAB_HOME需事先在环境变量中定义
        sudo docker run --detach \
        --hostname gitlab.example.com \
        --publish 443:443 --publish 80:80 --publish 22:22 \
        --name gitlab \
        --restart always \
        --volume $GITLAB_HOME/config:/etc/gitlab \
        --volume $GITLAB_HOME/logs:/var/log/gitlab \
        --volume $GITLAB_HOME/data:/var/opt/gitlab \
        gitlab/gitlab-ee:latest
        ```
    1. (__方法2__) 利用docker-compose
        1. 新建docker-compose.yml文件
            ```yml
            web:
            image: 'gitlab/gitlab-ee:latest'
            restart: always
            container_name: gitlab 
                #定义生成container的名字。如果缺省，docker-compose会自定义container名
            hostname: 'gitlab.example.com'
            environment:
                # Add any other gitlab.rb configuration here, each on its own line
                GITLAB_OMNIBUS_CONFIG: |
                external_url 'https://gitlab.example.com'
                    
            ports:
                - '80:80'
                - '443:443'
                - '22:22'
            volumes:
                - '$GITLAB_HOME/config:/etc/gitlab'
                - '$GITLAB_HOME/logs:/var/log/gitlab'
                - '$GITLAB_HOME/data:/var/opt/gitlab'
            ```
        1. 运行docker-compose  
            （<font color=red>_实际运行docker-compose并未成功。可以运行，并在本地访问。但无法在其他电脑上访问_</font>）
            ```bash
            docker-compose up -d
            ```
3. root密码重设
    1. 进入container
        ```bash
        docker exec -it container_id bash
        ```
    1. 进入DB
        ```bash
        gitlab-rails console -e production
        ```
    2. 重设root密码
        ```
        user = User.where(id: 1).first
        user.password = 'パスワード'
        user.password_confirmation = 'パスワード'
        user.save!
        ```
