package dataAccessLayer.entities;

import java.util.HashSet;
import java.util.Set;

import javax.persistence.*;

@Entity
public class File{
    @Id
    String name;
    int europaid;
    String notes;
    @ManyToMany
    Set<Location>locations=new HashSet();
}
