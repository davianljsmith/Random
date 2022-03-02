### Commands

`terraform init` 

Initialize infrastructure from the *.tf file(s).  Downloads the plugin(s) based on the provider(s) listed in the tf file(s).

`terraform plan` 

Displays the changes that will be made to the environment once applied. Makes changes based on the resources in the *.tf

`terraform apply` 

Applies the changes 

`terraform refresh` 

If there were manual changes, or any changes made by drift...refresh sets environment to state of terraform

`terraform destroy` 
`terraform destroy -target aws_instance.myec2`

Destroys infrastructure built by apply.  Use '-target' to destroy specific resource, listed as resource_type.resource_name.

__________________________________________________________________________________________________________________


save plan output to file

`terraform plan | tee -a outfile`

remove ANSI escape and color characters

`cat outfile | gsed -r "s/[[:cntrl:]]\[[0-9]{1,3}m//g" > outfileclean`

##### grep for additions/modifications/removals

`cat outfileclean | grep -e "^  +" -e "^  ~" -e "^  -"`

##### generate param string to tack to 'terraform apply' with pre-populated targets
##### note: modify grep expressions according to your need

`cat outfileclean | grep -e "^  +" -e "^  ~" -e "^  -" | grep launch_template | awk '{print $2}' | sed 's/^/-target /' | xargs`

__________________________________________________________________________________________________________

### Version Constraints

= (or no operator): Allows only one exact version number. Cannot be combined with other conditions.

!=: Excludes an exact version number.

>, >=, <, <=: Comparisons against a specified version, allowing versions for which the comparison is true. "Greater-than" requests newer versions, and "less-than" requests older versions.

~>: Allows only the rightmost version component to increment. For example, to allow new patch releases within a specific minor release, use the full version number: ~> 1.0.4 will allow installation of 1.0.5 and 1.0.10 but not 1.1.0. This is usually called the pessimistic constraint operator.



State file

terraform.tfstate

terraform.tfstate.backup


