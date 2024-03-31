## Awesome
- [Awesome SSH](https://github.com/moul/awesome-ssh#awesome-ssh- "Awesome SSH")
- [awesome-tunneling](https://github.com/anderspitman/awesome-tunneling#readme "awesome-tunneling")
## config
- [.ssh config](https://penpen-dev.com/blog/userknownhostsfile-stricthostkeychecking ".ssh config")
- [command](https://zenn.dev/ymmmtym/articles/useful-ssh-config-and-command "command")
```
cat ./.ssh/config 
Host *staging*
  StrictHostKeyChecking no
  # UserKnownHostsFile=~/.ssh/known_hosts_staging

Host *prod*
  StrictHostKeyChecking no
  # UserKnownHostsFile=~/.ssh/known_hosts_prod

Host *
  StrictHostKeyChecking no
  UserKnownHostsFile=/dev/null
  ServerAliveInterval 120
  ServerAliveCountMax 5
  AddKeysToAgent yes
  UseKeychain yes
  IdentitiesOnly yes
  TCPKeepAlive yes

# github
Host github
  HostName github.com
  User git
  Port 22
  IdentityFile ~/.ssh/***

# dev
HOST project-dev
  HostName project.dev.jp
  User ubuntu
  Port 443
  IdentityFile ~/.ssh/project.dev.pem

# staging
HOST project-staging
  HostName project.staging.jp
  User ubuntu
  Port 443
  IdentityFile ~/.ssh/project.staging.pem

# prod
HOST project-prod
  HostName project.prod.jp
  User ubuntu
  Port 443
  IdentityFile ~/.ssh/project.prod.pem
```