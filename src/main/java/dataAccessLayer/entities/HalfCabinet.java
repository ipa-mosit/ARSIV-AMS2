package dataAccessLayer.entities;

import java.util.HashSet;
import java.util.Set;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.OneToMany;

@Entity
public class HalfCabinet{
    @Id
    int id;
    int kabinNo;
    char kabinKisim;
    @OneToMany(mappedBy="halfCabinet")
    Set<Location> locations = new HashSet<Location>();
}
